#!/usr/bin/env python
##################################
'''
HXMT pipeline, run python hpipeline.py -h for help.

NOTE: this script is suitable for HXMTDAS v2.01, v2.02,
check out "http://code.ihep.ac.cn/hxmthsdc/hxmt_pipeline" for details.
'''
import argparse
import os
import sys
import glob
from astropy.io import fits

def energy_to_pi(energy, instrument, **kw):
    """
    calculate the PI channel based on EC relation
        LE:
        PI =  int(1536*(energy-0.1)/13);
        ME:
        PI = 1024*(energy-3)/60
        HE(only available in v2.04):
        PI=256(E-15)/370

    parameters
        energy : float
            the energy to calculate the PI channel

        instrument : string
            the instrument to calculate the energy_to_pi

    return 
        PI : int
            PI channel of corresponding energy
    """
    if energy == None:
        return 

    if instrument == "HE":
        if kw['version'] == '2.04':
            if (energy < 27) or (energy > 250):
                raise IOError("The HE instrument does not produce a light curve of {} keV, \
                        please select the energy range again.".format(energy))
            PI = int(256*(energy-15)/370)
        else:
            raise IOError("HXMT version {} does not support Energy to PI for HE instrument".format(kw['version']))
    elif instrument == "ME":
        if (energy < 10) or (energy > 35):
            raise IOError("The ME instrument does not produce a light curve of {} keV, \
                    please select the energy range again.".format(energy))
        PI = int(1024*(energy-3)/60)
    elif instrument == "LE":
        if (energy < 1) or (energy > 10):
            raise IOError("The LE instrument does not produce a light curve of {} keV, \
                    please select the energy range again.".format(energy))
        PI =  int(1536*(energy-0.1)/13)

    return PI



def get_dir(product_dir, instrument="HE"):
    if instrument == "HE":
        #TODO:use os.path.join instead of '/'
        aux_dir = product_dir    # AUX path
        acs_dir = product_dir    # ACS path
        he_dir = product_dir     # HE  path
        clean_dir = product_dir  # HE cleaned data path
        tmp_dir = product_dir    # HE temporary data
        spec_dir = product_dir   # spectra results path
        lc_dir = product_dir     # light curve results path
        rsp_dir = product_dir    # RSP results path
    
        #make directory for data structure
        if not os.path.isdir(product_dir):os.system('mkdir -p '+product_dir)
        if not os.path.isdir(aux_dir):os.system('mkdir -p ' +aux_dir)
        if not os.path.isdir(acs_dir):os.system('mkdir -p ' +acs_dir)
        if not os.path.isdir(he_dir):os.system('mkdir -p '+he_dir)
        if not os.path.isdir(clean_dir):os.system('mkdir -p '+clean_dir)
        if not os.path.isdir(tmp_dir):os.system('mkdir -p '+tmp_dir)
        if not os.path.isdir(spec_dir):os.system('mkdir -p '+spec_dir)
        if not os.path.isdir(lc_dir):os.system('mkdir -p '+lc_dir)
        if not os.path.isdir(rsp_dir):os.system('mkdir -p '+rsp_dir)
    
        dir_name = ["aux", "acs", "he", "clean", "tmp", "spectra", "lightcurves", "response"]
        dir_content = [aux_dir, acs_dir, he_dir, clean_dir, tmp_dir, spec_dir, lc_dir, rsp_dir]
        dir_dict= dict(zip(dir_name, dir_content))
        return dir_dict

    if instrument == "ME":
        aux_dir = product_dir      # AUX path
        acs_dir = product_dir      # ACS path
        me_dir = product_dir       # ME  path
        clean_dir = product_dir    # ME cleaned data path
        tmp_dir = product_dir      # ME temporary data
        spec_dir = product_dir     # spectra results path
        lc_dir = product_dir       # light curve results path
        rsp_dir = product_dir      # RSP results path
    
        #make directory for data structure
        if not os.path.isdir(product_dir):os.system('mkdir -p '+product_dir)
        if not os.path.isdir(aux_dir):os.system('mkdir -p ' +aux_dir)
        if not os.path.isdir(acs_dir):os.system('mkdir -p ' +acs_dir)
        if not os.path.isdir(me_dir):os.system('mkdir -p '+me_dir)
        if not os.path.isdir(clean_dir):os.system('mkdir -p '+clean_dir)
        if not os.path.isdir(tmp_dir):os.system('mkdir -p '+tmp_dir)
        if not os.path.isdir(spec_dir):os.system('mkdir -p '+spec_dir)
        if not os.path.isdir(lc_dir):os.system('mkdir -p '+lc_dir)
        if not os.path.isdir(rsp_dir):os.system('mkdir -p '+rsp_dir)
    
        dir_name = ["aux", "acs", "me", "clean", "tmp", "spectra", "lightcurves", "response"]
        dir_content = [aux_dir, acs_dir, me_dir, clean_dir, tmp_dir, spec_dir, lc_dir, rsp_dir]
        dir_dict= dict(zip(dir_name, dir_content))
        return dir_dict

    if instrument == "LE":
        aux_dir = product_dir       # AUX path
        acs_dir = product_dir       # ACS path
        le_dir = product_dir        # LE  path
        clean_dir = product_dir     # LE cleaned data path
        tmp_dir = product_dir       # LE temporary data
        spec_dir = product_dir      # spectra results path
        lc_dir = product_dir        # light curve results path
        rsp_dir = product_dir       # RSP results path
    
        #make directory for data structure
        if not os.path.isdir(product_dir):os.system('mkdir -p '+product_dir)
        if not os.path.isdir(aux_dir):os.system('mkdir -p ' +aux_dir)
        if not os.path.isdir(acs_dir):os.system('mkdir -p ' +acs_dir)
        if not os.path.isdir(le_dir):os.system('mkdir -p '+le_dir)
        if not os.path.isdir(clean_dir):os.system('mkdir -p '+clean_dir)
        if not os.path.isdir(tmp_dir):os.system('mkdir -p '+tmp_dir)
        if not os.path.isdir(spec_dir):os.system('mkdir -p '+spec_dir)
        if not os.path.isdir(lc_dir):os.system('mkdir -p '+lc_dir)
        if not os.path.isdir(rsp_dir):os.system('mkdir -p '+rsp_dir)
    
        dir_name = ["aux", "acs", "le", "clean", "tmp", "spectra", "lightcurves", "response"]
        dir_content = [aux_dir, acs_dir, le_dir, clean_dir, tmp_dir, spec_dir, lc_dir, rsp_dir]
        dir_dict= dict(zip(dir_name, dir_content))
        return dir_dict

def clean_data(data_dict, dir_dict, **kw):
    prefix = get_expID(data_dict)
    rmfile = []
    rmfile.append(os.path.join(dir_dict["tmp"], prefix+"_HE_pi.fits"))
    rmfile.append(os.path.join(dir_dict["tmp"], prefix+"_ME_pi.fits"))
    rmfile.append(os.path.join(dir_dict["tmp"], prefix+"_LE_pi.fits"))
    rmfile.append(os.path.join(dir_dict["tmp"], prefix+"_ME_grade.fits"))
    rmfile.append(os.path.join(dir_dict["tmp"], prefix+"_LE_recon.fits"))
    rmfile.append(os.path.join(dir_dict["lightcurves"], prefix+"_HE_lc.txt"))
    rmfile.append(os.path.join(dir_dict["spectra"], prefix+"_HE_spec.txt")   )
    rmfile.append(os.path.join(dir_dict["lightcurves"], prefix+"_ME_lc.txt") )
    rmfile.append(os.path.join(dir_dict["spectra"], prefix+"_ME_spec.txt")   )
    rmfile.append(os.path.join(dir_dict["lightcurves"], prefix+"_LE_lc.txt") )
    rmfile.append(os.path.join(dir_dict["spectra"], prefix+"_LE_spec.txt")   )
    if kw['version'] == '2.02':
        rmfile.append(os.path.join(dir_dict["spectra"], prefix+"_HE_merge_speclist.txt"))
        rmfile.append(os.path.join(dir_dict["spectra"], prefix+"_HE_merge_bkglist.txt"))
        rmfile.append(os.path.join(dir_dict["response"], prefix+"_HE_merge_rsplist.txt"))
    clean_data_cmd = 'rm -rf ' + ' '.join(rmfile)
    if kw['parallel_flag']:
        pfiles = os.path.join(dir_dict['tmp'], prefix+".tmp", "pfiles")
        clean_data_cmd = clean_data_cmd + ';rm -rf ' + pfiles
    return clean_data_cmd

def parallel(data_dict, dir_dict, **kw):
    """
    reference: https://heasarc.gsfc.nasa.gov/lheasoft/scripting.html

    """
    parallel_cmd = []
    prefix = get_expID(data_dict)
    pfile_dir = os.path.join(dir_dict['tmp'], prefix+".tmp", "pfiles")
    if not os.path.isdir(pfile_dir):
        os.system('mkdir -p ' + pfile_dir)
    parallel_cmd.append('export PFILES="%s;$HEADAS/syspfiles"'%(pfile_dir))
    parallel_cmd.append("export HEADASNOQUERY=")
    parallel_cmd.append("export HEADASPROMPT=/dev/null")
    return parallel_cmd


def get_rawdata(data_dir, instrument="HE"):
    #read filenames
    if instrument == "HE":
        try:filename     = sorted(glob.glob(data_dir + '/HE/*HE-Evt_FFFFFF_V[1-9]*'))[-1]
        except:print("\nERROR: Event file(Evt) not exist...skip this observation\n");
        try:orbitname    = sorted(glob.glob(data_dir + '/ACS/*_Orbit_*V[1-9]*'))[-1]
        except:print("\nERROR: Orbit file(Orbit) not exist...skip this observation\n");
        try:attname      = sorted(glob.glob(data_dir + '/ACS/*_Att_*V[1-9]*'))[-1]
        except:print("\nERROR: Attitude file(Att) not exist...skip this observation\n");
        try:hvfilename   = sorted(glob.glob(data_dir + '/HE/HXMT*HV_FFFFFF*V[1-9]*'))[-1]
        except:print("\nERROR: High Voltage file(HV) not exist...skip this observation\n");
        try:pmfilename   = sorted(glob.glob(data_dir + '/HE/HXMT*PM_FFFFFF*V[1-9]*'))[-1]
        except:print("\nERROR: Particle Monitor file(PM) not exist...skip this observation\n");
        try:deadfilename = sorted(glob.glob(data_dir + '/HE/HXMT*DTime*V[1-9]*'))[-1]
        except:print("\nERROR: Dead time file(DTime) not exist...skip this observation\n");
        try:tempfilename = sorted(glob.glob(data_dir + '/HE/HXMT*TH*V[1-9]*'))[-1]
        except:print("\nERROR: Temperature file(TH) not exist...skip this observation\n");
        try:ehkfilename  = sorted(glob.glob(data_dir + '/AUX/*_EHK_*V[1-9]*'))[-1]
        except:print("\nERROR: House Keeping file(EHK) not exist...skip this observation\n");

        rawdata_name = ["Evt", "Orbit", "Att", "HV", "PM", "DTime", "TH", "EHK"]
        rawdata_content = [filename, orbitname, attname, hvfilename, pmfilename, deadfilename, tempfilename, ehkfilename]
        rawdata_dict = dict(zip(rawdata_name, rawdata_content))

        return rawdata_dict

    elif instrument == "ME":

        try:filename     = sorted(glob.glob(data_dir + '/ME/*ME-Evt_FFFFFF_V[1-9]*'))[-1]
        except:print("\nERROR: Event file(Evt) not exist...skip this observation\n");
        try:orbitname    = sorted(glob.glob(data_dir + '/ACS/*_Orbit_*V[1-9]*'))[-1]
        except:print("\nERROR: Orbit file(Orbit) not exist...skip this observation\n");
        try:attname      = sorted(glob.glob(data_dir + '/ACS/*_Att_*V[1-9]*'))[-1]
        except:print("\nERROR: Attitude file(Att) not exist...skip this observation\n");
        try:tempfilename = sorted(glob.glob(data_dir + '/ME/HXMT*TH*V[1-9]*'))[-1]
        except:print("\nERROR: Temperature file(TH) not exist...skip this observation\n");
        try:instatname   = sorted(glob.glob(data_dir + '/ME/HXMT*InsStat*V[1-9]*'))[-1]
        except:print("\nERROR: Instrument Status file(InsStat) not exist...skip this observation\n");
        try:ehkfilename  = sorted(glob.glob(data_dir + '/AUX/*_EHK_*V[1-9]*'))[-1]
        except:print("\nERROR: House Keeping file(EHK) not exist...skip this observation\n");

        rawdata_name = ["Evt", "Orbit", "Att", "TH", "EHK", "InsStat"]
        rawdata_content = [filename, orbitname, attname, tempfilename, ehkfilename, instatname]
        rawdata_dict = dict(zip(rawdata_name, rawdata_content))

        return rawdata_dict

    elif instrument == "LE":

        try:filename     = sorted(glob.glob(data_dir + '/LE/*LE-Evt_FFFFFF_V[1-9]*'))[-1]
        except:print("\nERROR: Event file(Evt) not exist...skip this observation\n");
        try:orbitname    = sorted(glob.glob(data_dir + '/ACS/*_Orbit_*V[1-9]*'))[-1]
        except:print("\nERROR: Orbit file(Orbit) not exist...skip this observation\n");
        try:attname      = sorted(glob.glob(data_dir + '/ACS/*_Att_*V[1-9]*'))[-1]
        except:print("\nERROR: Attitude file(Att) not exist...skip this observation\n");
        try:tempfilename = sorted(glob.glob(data_dir + '/LE/HXMT*TH*V[1-9]*'))[-1]
        except:print("\nERROR: Temperature file(TH) not exist...skip this observation\n");
        try:instatname   = sorted(glob.glob(data_dir + '/LE/HXMT*InsStat*V[1-9]*'))[-1]
        except:print("\nERROR: Instrument Status file(InsStat) not exist...skip this observation\n");
        try:ehkfilename  = sorted(glob.glob(data_dir + '/AUX/*_EHK_*V[1-9]*'))[-1]
        except:print("\nERROR: House Keeping file(EHK) not exist...skip this observation\n");

        rawdata_name = ["Evt", "Orbit", "Att", "TH", "EHK", "InsStat"]
        rawdata_content = [filename, orbitname, attname, tempfilename, ehkfilename, instatname]
        rawdata_dict = dict(zip(rawdata_name, rawdata_content))

        return rawdata_dict

def hepical(data_dict, dir_dict):
    evtfile = data_dict["Evt"]
    prefix = get_expID(data_dict)
    outfile = os.path.join(dir_dict["tmp"], prefix+"_HE_pi.fits")
    hepical_cmd = 'hepical evtfile="%s" outfile="%s" minpulsewidth=54 maxpulsewidth=70 clobber=yes'%(evtfile, outfile)
    return hepical_cmd

def mepical(data_dict, dir_dict):
    evtfile = data_dict["Evt"]
    tempfile= data_dict["TH"]
    prefix = get_expID(data_dict)
    outfile = os.path.join(dir_dict["tmp"], prefix+"_ME_pi.fits")
    mepical_cmd = 'mepical evtfile="%s" tempfile="%s" outfile="%s" '\
            'clobber=yes history=yes'%(evtfile, tempfile, outfile)
    return mepical_cmd

def lepical(data_dict, dir_dict):
    evtfile = data_dict["Evt"]
    tempfile= data_dict["TH"]
    prefix = get_expID(data_dict)
    outfile = os.path.join(dir_dict["tmp"], prefix+"_LE_pi.fits")
    lepical_cmd = 'lepical evtfile="%s" tempfile="%s" outfile="%s" '\
            'clobber=yes history=yes'%(evtfile, tempfile, outfile)
    return lepical_cmd

def hegtigen(data_dict, dir_dict):
    hvfile = data_dict["HV"]
    tempfile = data_dict["TH"]
    pmfile = data_dict["PM"]
    ehkfile = data_dict["EHK"]
    prefix = get_expID(data_dict)
    outfile = os.path.join(dir_dict["tmp"], prefix+"_HE_gti.fits")
    hegtigen_cmd = 'hegtigen hvfile="%s" tempfile="%s" pmfile="%s" outfile="%s" '\
    'ehkfile="%s" defaultexpr=NONE expr="ELV>10&&COR>8&&SAA_FLAG==0&&TN_SAA>300&&T_SAA>300&&ANG_DIST<=0.04" '\
    'pmexpr="" clobber=yes history=yes'%(hvfile, tempfile, pmfile, outfile, ehkfile)
    return hegtigen_cmd

def megtigen(data_dict, dir_dict):
    megtigen_cmd = []
    tempfile = data_dict["TH"]
    ehkfile = data_dict["EHK"]
    prefix = get_expID(data_dict)
    outfile = os.path.join(dir_dict["tmp"], prefix+"_ME_gti_tmp.fits")
    newgtifile = os.path.join(dir_dict["tmp"], prefix+"_ME_gti.fits")
    megtigen_cmd.append('megtigen tempfile="%s" ehkfile="%s" outfile="%s" '\
            'defaultexpr=NONE expr="ELV>10&&COR>8&&SAA_FLAG==0&&T_SAA>300&&TN_SAA>300&&ANG_DIST<=0.04" '\
            'clobber=yes history=yes'%(tempfile, ehkfile, outfile))
    #new le gti
    gradefile  = os.path.join(dir_dict["tmp"], prefix+"_ME_grade.fits")
    baddetector= "$HEADAS/refdata/medetectorstatus.fits"
    newstatus  = os.path.join(dir_dict["tmp"], prefix+"_ME_status.fits")
    newgti_cmd = 'megti %s %s %s %s %s'%(gradefile, outfile, newgtifile, baddetector, newstatus)
    megtigen_cmd.append(newgti_cmd)
    return megtigen_cmd

def legtigen(data_dict, dir_dict):
    legtigen_cmd = []
    eventfile= data_dict["Evt"]
    tempfile = data_dict["TH"]
    ehkfile = data_dict["EHK"]
    instatfile = data_dict["InsStat"]
    prefix = get_expID(data_dict)
    outfile = os.path.join(dir_dict["tmp"], prefix+"_LE_gti_tmp.fits")
    newgtifile = os.path.join(dir_dict["tmp"], prefix+"_LE_gti.fits")
    legtigen_cmd.append('legtigen evtfile="%s" instatusfile="%s" tempfile="%s" ehkfile="%s" '\
            'outfile="%s" defaultexpr=NONE expr="ELV>10&&DYE_ELV>30&&COR>8&&SAA_FLAG==0&&T_SAA>=300&&TN_SAA>=300&&ANG_DIST<=0.04" '\
            'clobber=yes history=yes'%("NONE", instatfile, tempfile, ehkfile, outfile))
    #new le gti
    reconfile = os.path.join(dir_dict["tmp"], prefix+"_LE_recon.fits")
    newgti_cmd = 'legti %s %s %s'%(reconfile, outfile, newgtifile)
    legtigen_cmd.append(newgti_cmd)
    return legtigen_cmd

def megrade(data_dict, dir_dict):
    prefix = get_expID(data_dict)
    pifile = os.path.join(dir_dict["tmp"], prefix+"_ME_pi.fits")
    outfile = os.path.join(dir_dict["tmp"], prefix+"_ME_grade.fits")
    deadfile = os.path.join(dir_dict["tmp"], prefix+"_ME_dtime.fits")
    megrade_cmd = 'megrade evtfile="%s" outfile="%s" deadfile="%s" binsize=1 '\
            'clobber=yes history=yes'%(pifile, outfile, deadfile)
    return megrade_cmd

def lerecon(data_dict, dir_dict):
    prefix = get_expID(data_dict)
    pifile = os.path.join(dir_dict["tmp"], prefix+"_LE_pi.fits")
    outfile = os.path.join(dir_dict["tmp"], prefix+"_LE_recon.fits")
    instatfile = data_dict["InsStat"]
    lerecon_cmd = 'lerecon evtfile="%s" outfile="%s" instatusfile="%s" clobber=yes history=yes'%(
            pifile, outfile, instatfile)
    return lerecon_cmd

def hescreen(data_dict, dir_dict):
    prefix = get_expID(data_dict)
    pifile = os.path.join(dir_dict["tmp"], prefix+"_HE_pi.fits")
    gtifile  = os.path.join(dir_dict["tmp"], prefix+"_HE_gti.fits")
    screenfile  = os.path.join(dir_dict["clean"], prefix+"_HE_screen.fits")
    userdetid = "0-17"
    hescreen_cmd = 'hescreen evtfile="%s" gtifile="%s" outfile="%s" '\
    'userdetid="%s" eventtype=1 anticoincidence=yes '\
    'starttime=0 stoptime=0 minPI=0 maxPI=255 '\
    ' clobber=yes history=yes'%(pifile, gtifile, screenfile, userdetid)
    return hescreen_cmd

def mescreen(data_dict, dir_dict):
    prefix = get_expID(data_dict)
    pifile = os.path.join(dir_dict["tmp"], prefix+"_ME_grade.fits")
    gtifile  = os.path.join(dir_dict["tmp"], prefix+"_ME_gti.fits")
    outfile  = os.path.join(dir_dict["clean"], prefix+"_ME_screen.fits")
    statusfile = os.path.join(dir_dict["tmp"], prefix+"_ME_status.fits")
    userdetid = "0-53"
    mescreen_cmd = 'mescreen evtfile="%s" gtifile="%s" outfile="%s" baddetfile="%s" '\
    'userdetid="%s" starttime=0 stoptime=0 minPI=0 maxPI=1023 clobber=yes'%(
            pifile, gtifile, outfile, statusfile, userdetid)
    return mescreen_cmd

def lescreen(data_dict, dir_dict):
    prefix = get_expID(data_dict)
    pifile = os.path.join(dir_dict["tmp"], prefix+"_LE_recon.fits")
    gtifile  = os.path.join(dir_dict["tmp"], prefix+"_LE_gti.fits")
    outfile  = os.path.join(dir_dict["clean"], prefix+"_LE_screen.fits")
    userdetid = "0-95"
    lescreen_cmd = 'lescreen evtfile="%s" gtifile="%s" outfile="%s" userdetid="%s" '\
            'eventtype=0 starttime=0 stoptime=0 minPI=0 maxPI=1535 '\
            'clobber=yes history=yes'%(
                    pifile, gtifile, outfile, userdetid)
    return lescreen_cmd

def helcgen(data_dict, dir_dict, binsize=1, minE=27, maxE=250, **kw):
    minPI = energy_to_pi(minE, instrument="HE", version=kw['version'])
    maxPI = energy_to_pi(maxE, instrument="HE", version=kw['version'])
    prefix = get_expID(data_dict)
    screenfile  = os.path.join(dir_dict["clean"], prefix+"_HE_screen.fits")
    outfile     = os.path.join(dir_dict["lightcurves"], prefix+"_HE_lc")
    deadfile    = data_dict["DTime"]
    helcgen_cmd = 'helcgen evtfile="%s" outfile="%s" '\
            'deadfile="%s" userdetid='\
            '"0-15,17" binsize=%s starttime=0 '\
            'stoptime=0 minPI=%s maxPI=%s deadcorr=yes clobber=yes'%(screenfile, outfile, deadfile, 
                    str(binsize),str(minPI), str(maxPI))
    return helcgen_cmd

def melcgen(data_dict, dir_dict, binsize=1, minE=10, maxE=35):
    #NOTE:2.04 update -- energy range selection (energy to PI)
    minPI = energy_to_pi(minE, instrument="ME")
    maxPI = energy_to_pi(maxE, instrument="ME")

    prefix = get_expID(data_dict)
    screenfile  = os.path.join(dir_dict["clean"], prefix+"_ME_screen.fits")
    outfile     = os.path.join(dir_dict["lightcurves"], prefix+"_ME_lc")
    deadfile    = os.path.join(dir_dict["tmp"], prefix+"_ME_dtime.fits")
    userdetid   = "0-7,11-25,29-43,47-53"
    melcgen_cmd = 'melcgen evtfile="%s" outfile="%s" deadfile="%s" '\
            'userdetid="%s" binsize=%s starttime=0 stoptime=0 '\
            'minPI="%s" maxPI="%s" deadcorr=yes clobber=yes'%(
                    screenfile, outfile, deadfile, userdetid, str(binsize), str(minPI), str(maxPI))
    return melcgen_cmd

def lelcgen(data_dict, dir_dict, binsize=1, minE=1, maxE=10):
    #NOTE:2.04 update -- energy range selection (energy to PI)
    minPI = energy_to_pi(minE, instrument="LE")
    maxPI = energy_to_pi(maxE, instrument="LE")

    prefix = get_expID(data_dict)
    screenfile  = os.path.join(dir_dict["clean"], prefix+"_LE_screen.fits")
    outfile     = os.path.join(dir_dict["lightcurves"], prefix+"_LE_lc")
    userdetid   = "0,2-4,6-10,12,14,20,22-26,28,30,32,34-36,38-42,44,46,52,54-58,60-62,64,66-68,70-74,76,78,84,86,88-90,92-94"
    lelcgen_cmd = 'lelcgen evtfile="%s" outfile="%s" '\
            'userdetid="%s" binsize=%s starttime=0 stoptime=0 '\
            'minPI=%s maxPI=%s eventtype=1 clobber=yes'%(
                    screenfile, outfile, userdetid, str(binsize), str(minPI), str(maxPI))
    return lelcgen_cmd

def hespecgen(data_dict, dir_dict, **kw):
    prefix = get_expID(data_dict)
    screenfile  = os.path.join(dir_dict["clean"], prefix+"_HE_screen.fits")
    outfile     = os.path.join(dir_dict["spectra"], prefix+"_HE_spec")
    deadfile    = data_dict["DTime"]
    if 'version' in kw:
        if kw['version'] == '2.04':
        #NOTE:2.04 update -- userdetid selection 
            hespecgen_cmd = 'hespecgen evtfile="%s" outfile="%s" '\
                    'deadfile="%s" userdetid='\
                    '"0-15,17" eventtype=1 starttime=0 '\
                    'stoptime=0 minPI=0 maxPI=255 clobber=yes'%(screenfile, outfile, deadfile)
        elif kw['version'] == '2.02':
            hespecgen_cmd = 'hespecgen evtfile="%s" outfile="%s" '\
                    'deadfile="%s" userdetid='\
                    '"0;1;2;3;4;5;6;7;8;9;10;11;12;13;14;15;16;17" eventtype=1 starttime=0 '\
                    'stoptime=0 minPI=0 maxPI=255 clobber=yes'%(screenfile, outfile, deadfile)
            print(hespecgen_cmd)
    else:
        # default is v2.04
        hespecgen_cmd = 'hespecgen evtfile="%s" outfile="%s" '\
                'deadfile="%s" userdetid='\
                '"0-15,17" eventtype=1 starttime=0 '\
                'stoptime=0 minPI=0 maxPI=255 clobber=yes'%(screenfile, outfile, deadfile)
    return hespecgen_cmd

def mespecgen(data_dict, dir_dict):
    prefix = get_expID(data_dict)
    screenfile  = os.path.join(dir_dict["clean"], prefix+"_ME_screen.fits")
    outfile     = os.path.join(dir_dict["spectra"], prefix+"_ME_spec")
    deadfile    = os.path.join(dir_dict["tmp"], prefix+"_ME_dtime.fits")
    userdetid   = "0-7,11-25,29-43,47-53"
    mespecgen_cmd = 'mespecgen evtfile="%s" outfile="%s" '\
            'deadfile="%s" userdetid="%s" '\
            'starttime=0 stoptime=0 minPI=0 maxPI=1023'%(
                    screenfile, outfile, deadfile,userdetid)
    return mespecgen_cmd

def lespecgen(data_dict, dir_dict):
    prefix = get_expID(data_dict)
    screenfile  = os.path.join(dir_dict["clean"], prefix+"_LE_screen.fits")
    outfile     = os.path.join(dir_dict["spectra"], prefix+"_LE_spec")
    userdetid   = "0,2-4,6-10,12,14,20,22-26,28,30,32,34-36,38-42,"\
            "44,46,52,54-58,60-62,64,66-68,70-74,76,78,84,86,88-90,92-94"
    lespecgen_cmd = 'lespecgen evtfile="%s" outfile="%s" '\
            'eventtype=1 userdetid="%s" '\
            'starttime=0 stoptime=0 minPI=0 maxPI=1535'%(
                    screenfile, outfile, userdetid)
    return lespecgen_cmd



def herspgen(data_dict, dir_dict, ra=-1, dec=-91, **kw):
    herspgen_cmd = []
    prefix = get_expID(data_dict)

    if 'version' in kw:
        if kw['version'] == '2.04':
            # v2.04 update: spectrum file is fixed to g0-17
            phafile = os.path.join(dir_dict["spectra"], prefix+"_HE_spec_g0_0-17.pha")
            phafilename = os.path.basename(phafile)
            rspfilename = phafilename.replace("spec", "rsp")
            rspfilename = rspfilename.replace("pha", "fits")
            outfile = os.path.join(dir_dict["response"], rspfilename)
            attfile = data_dict["Att"]
            rsp_cmd = 'herspgen phafile="%s" outfile="%s" attfile="%s" ra="%s" dec="%s" clobber=yes'%(phafile, outfile, attfile, str(ra), str(dec))
            herspgen_cmd.append(rsp_cmd)
        elif kw['version'] == '2.02':
            #phafile = os.path.join(dir_dict["spectra"], prefix+"_HE_spec_g%s_%s.pha"%(str(i),str(i)))
            #phafile_list = glob.glob(os.path.join(dir_dict["spectra"], prefix+"_HE_spec*.pha"))
            for i in range(18):
                if i == 16:
                    continue
                else:
                    phafile = os.path.join(dir_dict["spectra"], prefix+"_HE_spec_g%s_%s.pha"%(str(i),str(i)))
                phafilename = os.path.basename(phafile)
                rspfilename = phafilename.replace("spec", "rsp")
                rspfilename = rspfilename.replace("pha", "fits")
                outfile = os.path.join(dir_dict["response"], rspfilename)
                attfile = data_dict["Att"]
                rsp_cmd = 'herspgen phafile="%s" outfile="%s" attfile="%s" ra="%s" dec="%s" clobber=yes'%(phafile, outfile, attfile, str(ra), str(dec))
                herspgen_cmd.append(rsp_cmd)

    else:
        #NOTE: default is 2.04
        phafile = os.path.join(dir_dict["spectra"], prefix+"_HE_spec_g0_0-17.pha")
    
        phafilename = os.path.basename(phafile)
        rspfilename = phafilename.replace("spec", "rsp")
        rspfilename = rspfilename.replace("pha", "fits")
        outfile = os.path.join(dir_dict["response"], rspfilename)
        attfile = data_dict["Att"]
        rsp_cmd = 'herspgen phafile="%s" outfile="%s" attfile="%s" ra="%s" dec="%s" clobber=yes'%(phafile, outfile, attfile, str(ra), str(dec))
        herspgen_cmd.append(rsp_cmd)

    return herspgen_cmd

def merspgen(data_dict, dir_dict, ra=-1, dec=-91):
    prefix = get_expID(data_dict)
    phafile = os.path.join(dir_dict["spectra"], prefix+"_ME_spec_g%s_%s.pha"%('0','0-53'))
    phafilename = os.path.basename(phafile)
    rspfilename = phafilename.replace("spec", "rsp")
    rspfilename = rspfilename.replace("pha", "fits")
    outfile = os.path.join(dir_dict["response"], rspfilename)
    attfile = data_dict["Att"]
    merspgen_cmd = 'merspgen phafile="%s" outfile="%s" attfile="%s" ra="%s" dec="%s" clobber=yes'%(phafile, outfile, attfile, str(ra), str(dec))
    return merspgen_cmd

def lerspgen(data_dict, dir_dict, ra=-1, dec=-91):
    prefix = get_expID(data_dict)
    phafile = os.path.join(dir_dict["spectra"], prefix+"_LE_spec_g%s_%s.pha"%('0','0-94'))
    phafilename = os.path.basename(phafile)
    rspfilename = phafilename.replace("spec", "rsp")
    rspfilename = rspfilename.replace("pha", "fits")
    outfile = os.path.join(dir_dict["response"], rspfilename)
    attfile = data_dict["Att"]
    tempfile = data_dict["TH"]
    lerspgen_cmd = 'lerspgen phafile="%s" outfile="%s" attfile="%s" tempfile="%s" ra="%s" dec="%s" clobber=yes'%(phafile, outfile, attfile, tempfile, str(ra), str(dec))
    return lerspgen_cmd

def hebkgmap(data_dict, dir_dict, flag='lc', minE=27, maxE=250, **kw):
    hebkgmap_cmd = []
    #NOTE: 2.04 update -- energy to PI 
    if kw['version'] == '2.04':
        minPI = energy_to_pi(minE, instrument="HE", version=kw['version'])
        maxPI = energy_to_pi(maxE, instrument="HE", version=kw['version'])
    elif kw['version'] == '2.02':
        minPI = 26
        maxPI = 120 
        print("Warning: version {} does not support Energy selection for HE instrument\
                minPI is fixed to 26 (~= 25 keV)\
                maxPI is fixed to 120 (~= 250 keV)".format(kw['version']))
    prefix = get_expID(data_dict)
    screenfile  = os.path.join(dir_dict["clean"], prefix+"_HE_screen.fits")
    ehkfile = data_dict["EHK"]
    gtifile = os.path.join(dir_dict["tmp"], prefix+"_HE_gti.fits")
    deadfile = data_dict["DTime"]
    if flag == 'lc':
        lcfile = os.path.join(dir_dict["lightcurves"], prefix+"_HE_lc_g0_0-17.lc")
        listfile = os.path.join(dir_dict["lightcurves"], prefix+"_HE_lc.txt")
        create_bkglist_cmd = "ls %s | sort -V > %s"%(lcfile,listfile)
        hebkgmap_cmd.append(create_bkglist_cmd)
        outfile = os.path.join(dir_dict["lightcurves"], prefix+"_HE_lcbkg")
        hebkgmap_cmd.append('hebkgmap lc %s %s %s %s %s %s %s %s'%(screenfile, ehkfile, gtifile,
                deadfile, listfile, str(minPI), str(maxPI), outfile))
    if flag == 'spec':
        #NOTE: spec does not selection energy range
        minPI = 0
        maxPI = 255
        specfile = os.path.join(dir_dict["spectra"], prefix+"_HE_spec_g*.pha")
        listfile = os.path.join(dir_dict["spectra"], prefix+"_HE_spec.txt")
        create_bkglist_cmd = "ls %s | sort -V > %s"%(specfile,listfile)
        hebkgmap_cmd.append(create_bkglist_cmd)
        outfile = os.path.join(dir_dict["spectra"], prefix+"_HE_specbkg")
        hebkgmap_cmd.append('hebkgmap spec %s %s %s %s %s %s %s %s'%(screenfile, ehkfile, gtifile,
                deadfile, listfile, str(minPI), str(maxPI), outfile))
    return hebkgmap_cmd

def mebkgmap(data_dict, dir_dict, flag='lc', minE=10, maxE=35, **kw):
    #NOTE: 2.04 update -- energy selection (energy to PI)
    minPI = energy_to_pi(minE, instrument="ME")
    maxPI = energy_to_pi(maxE, instrument="ME")

    mebkgmap_cmd = []
    prefix = get_expID(data_dict)
    screenfile  = os.path.join(dir_dict["clean"], prefix+"_ME_screen.fits")
    ehkfile = data_dict["EHK"]
    gtifile = os.path.join(dir_dict["tmp"], prefix+"_ME_gti.fits")
    deadfile = os.path.join(dir_dict["tmp"],prefix+"_ME_dtime.fits")
    baddetfile  = os.path.join(dir_dict["tmp"], prefix+"_ME_status.fits")
    tempfile = data_dict["TH"]
    if flag == 'lc':
        lcfile = os.path.join(dir_dict["lightcurves"], prefix+"_ME_lc_*.lc")
        listfile = os.path.join(dir_dict["lightcurves"], prefix+"_ME_lc.txt")
        create_bkglist_cmd = "ls %s | sort -V > %s"%(lcfile,listfile)
        mebkgmap_cmd.append(create_bkglist_cmd)
        outfile = os.path.join(dir_dict["lightcurves"], prefix+"_ME_lcbkg")
        mebkgmap_cmd.append('mebkgmap lc %s %s %s %s %s %s %s %s %s %s'%(
                    screenfile, ehkfile, gtifile, deadfile, tempfile, listfile, str(minPI), str(maxPI), outfile, baddetfile))
    if flag == 'spec':
        #NOTE: spec does not selection energy range
        minPI = 0
        maxPI = 1023
        specfile = os.path.join(dir_dict["spectra"], prefix+"_ME_spec_*.pha")
        listfile = os.path.join(dir_dict["spectra"], prefix+"_ME_spec.txt")
        create_bkglist_cmd = "ls %s | sort -V > %s"%(specfile,listfile)
        mebkgmap_cmd.append(create_bkglist_cmd)
        outfile = os.path.join(dir_dict["spectra"], prefix+"_ME_specbkg")
        mebkgmap_cmd.append('mebkgmap spec %s %s %s %s %s %s %s %s %s %s'%(
                    screenfile, ehkfile, gtifile, deadfile, tempfile, listfile, str(minPI), str(maxPI), outfile, baddetfile))
    return mebkgmap_cmd

def lebkgmap(data_dict, dir_dict, flag='lc', minE=1, maxE=10):
    #NOTE: 2.04 update -- energy selection (energy to PI)
    minPI = energy_to_pi(minE, instrument="LE")
    maxPI = energy_to_pi(maxE, instrument="LE")

    lebkgmap_cmd = []
    prefix = get_expID(data_dict)
    screenfile  = os.path.join(dir_dict["clean"], prefix+"_LE_screen.fits")
    ehkfile = data_dict["EHK"]
    gtifile = os.path.join(dir_dict["tmp"], prefix+"_LE_gti.fits")
    if flag == 'lc':
        lcfile = os.path.join(dir_dict["lightcurves"], prefix+"_LE_lc_*.lc")
        listfile = os.path.join(dir_dict["lightcurves"], prefix+"_LE_lc.txt")
        create_bkglist_cmd = "ls %s | sort -V > %s"%(lcfile,listfile)
        lebkgmap_cmd.append(create_bkglist_cmd)
        outfile = os.path.join(dir_dict["lightcurves"], prefix+"_LE_lcbkg")
        lebkgmap_cmd.append('lebkgmap lc %s %s %s %s %s %s'%(
                    screenfile, gtifile, listfile, str(minPI), str(maxPI), outfile))
    if flag == 'spec':
        #NOTE: spec does not selection energy range
        minPI = 0 
        maxPI = 1535
        specfile = os.path.join(dir_dict["spectra"], prefix+"_LE_spec_*.pha")
        listfile = os.path.join(dir_dict["spectra"], prefix+"_LE_spec.txt")
        create_bkglist_cmd = "ls %s | sort -V > %s"%(specfile,listfile)
        lebkgmap_cmd.append(create_bkglist_cmd)
        outfile = os.path.join(dir_dict["spectra"], prefix+"_LE_specbkg")
        lebkgmap_cmd.append('lebkgmap spec %s %s %s %s %s %s'%(
                    screenfile, gtifile, listfile, str(minPI), str(maxPI), outfile))
    return lebkgmap_cmd

def hxbary(data_dict, dir_dict, ra=-1, dec=-91, instrument="HE"):
    prefix = get_expID(data_dict)
    if instrument == "HE":
        screenfile = os.path.join(dir_dict["clean"], prefix+"_HE_screen.fits")
    elif instrument == "ME":
        screenfile = os.path.join(dir_dict["clean"], prefix+"_ME_screen.fits")
    elif instrument == "LE":
        screenfile = os.path.join(dir_dict["clean"], prefix+"_LE_screen.fits")
    orbitfile  = data_dict["Orbit"]
    hxbary_cmd = 'hxbary evtfile=%s orbitfile="%s" ra=%s dec=%s eph=2 clobber=yes'%(
            screenfile, orbitfile, str(ra), str(dec))
    return hxbary_cmd

def hhe_spec2pi(data_dict, dir_dict, **kw):
    hhe_spec2pi_cmd = []
    prefix = get_expID(data_dict)
    spec_files = os.path.join(dir_dict["spectra"], prefix+"_HE_spec_g*.pha")
    spec_list  = os.path.join(dir_dict["spectra"], prefix+"_HE_merge_speclist.txt")
    create_src_list_cmd = 'ls %s | sort -V | grep -v "_HE_spec_g16_16.pha" > %s'%(spec_files, spec_list)
    hhe_spec2pi_cmd.append(create_src_list_cmd)

    bkg_files = os.path.join(dir_dict["spectra"], prefix+"_HE_specbkg_*.pha")
    bkg_list  = os.path.join(dir_dict["spectra"], prefix+"_HE_merge_bkglist.txt")
    create_bkg_list_cmd = 'ls %s | sort -V | grep -v "_HE_specbkg_16.pha"> %s'%(bkg_files, bkg_list)
    hhe_spec2pi_cmd.append(create_bkg_list_cmd)

    rsp_files = os.path.join(dir_dict["response"], prefix+"_HE_rsp_g*.fits")
    rsp_list  = os.path.join(dir_dict["response"], prefix+"_HE_merge_rsplist.txt")
    create_rsp_list_cmd = 'ls %s | sort -V > %s'%(rsp_files, rsp_list)
    hhe_spec2pi_cmd.append(create_rsp_list_cmd)

    out_spec = os.path.join(dir_dict["spectra"], prefix+"_HE_spec_all.pha")
    out_bkg  = os.path.join(dir_dict["spectra"], prefix+"_HE_specbkg_all.pha")
    out_rsp  = os.path.join(dir_dict["spectra"], prefix+"_HE_rsp_all.fits")
    merge_HE_cmd = "hhe_spec2pi %s %s %s %s %s %s" % (spec_list, bkg_list, rsp_list, out_spec, out_bkg, out_rsp)
    hhe_spec2pi_cmd.append(merge_HE_cmd)
    
    return hhe_spec2pi_cmd

def get_expID(data_dict):
    #get the Exposure ID and assign as prefix for files
    evtfile = data_dict["Evt"]
    hdulist = fits.open(evtfile)
    exp_id = hdulist[1].header["EXP_ID"]
    exp_id = exp_id.split('-')
    exp_id = exp_id[0]
    return exp_id

def main(data_dir, product_dir, instrument="HE", ra=-1, dec=-91, bary_flag=False, version='2.04', **kw):
    # read raw data
    rawfiles = get_rawdata(data_dir,instrument=instrument)
    outdirs  = get_dir(product_dir, instrument=instrument)

    pipeline_commands = []
    if kw['parallel_flag']:
        pipeline_commands = pipeline_commands + parallel(rawfiles, outdirs)
    if instrument == "HE":
        #hepical
        hepical_cmd = hepical(rawfiles, outdirs)
        pipeline_commands.append(hepical_cmd)
        #hegtigen
        hegtigen_cmd = hegtigen(rawfiles, outdirs)
        pipeline_commands.append(hegtigen_cmd)
        #hescreen
        hescreen_cmd = hescreen(rawfiles, outdirs)
        pipeline_commands.append(hescreen_cmd)
        #helcgen
        #NOTE:2.04 update -- LC energy range selection
        if kw['he_lc_emin']:
            HE_LC_EMIN = kw['he_lc_emin']
        else:
            HE_LC_EMIN = 27
        if kw['he_lc_emax']:
            HE_LC_EMAX = kw['he_lc_emax']
        else:
            HE_LC_EMAX = 250
        if kw['he_lc_binsize']:
            HE_LC_BINSIZE = kw['he_lc_binsize']
        else:
            HE_LC_BINSIZE = 1
        helcgen_cmd = helcgen(rawfiles, outdirs, binsize=HE_LC_BINSIZE, minE=HE_LC_EMIN, maxE=HE_LC_EMAX, version=version)
        pipeline_commands.append(helcgen_cmd)
        #hespecgen
        hespecgen_cmd = hespecgen(rawfiles, outdirs, version=version)
        pipeline_commands.append(hespecgen_cmd)
        #herspgen
        herspgen_cmd = herspgen(rawfiles, outdirs, ra=ra, dec=dec, version=version)
        # herspgen is a list
        pipeline_commands = pipeline_commands + herspgen_cmd
        #hebkgmap for spec
        hebkgmap_cmd = hebkgmap(rawfiles, outdirs, flag="spec", minE=None, maxE=None, version=version)
        pipeline_commands = pipeline_commands + hebkgmap_cmd
        #hebkgmap for lc
        hebkgmap_cmd = hebkgmap(rawfiles, outdirs, flag="lc", minE=HE_LC_EMIN, maxE=HE_LC_EMAX, version=version)
        pipeline_commands = pipeline_commands + hebkgmap_cmd

        if version == 2.02:
            #hhe_spec2pi for spec
            hhe_spec2pi_cmd = hhe_spec2pi(rawfiles, outdirs)
            pipeline_commands = pipeline_commands + hhe_spec2pi_cmd

        if bary_flag:
            hxbary_cmd = hxbary(rawfiles, outdirs, ra=ra, dec=dec, instrument=instrument)
            pipeline_commands.append(hxbary_cmd)
    elif instrument == "ME":
        #mepical
        mepical_cmd = mepical(rawfiles, outdirs)
        pipeline_commands.append(mepical_cmd)
        #megrade
        megrade_cmd = megrade(rawfiles, outdirs)
        pipeline_commands.append(megrade_cmd)
        #megtigen
        megtigen_cmd = megtigen(rawfiles, outdirs)
        pipeline_commands = pipeline_commands + megtigen_cmd
        #mescreen
        mescreen_cmd = mescreen(rawfiles, outdirs)
        pipeline_commands.append(mescreen_cmd)
        #melcgen
        #NOTE:2.04 update -- LC energy range selection
        if kw['me_lc_emin']:
            ME_LC_EMIN = kw['me_lc_emin']
        else:
            ME_LC_EMIN = 10
        if kw['me_lc_emax']:
            ME_LC_EMAX = kw['me_lc_emax']
        else:
            ME_LC_EMAX = 35
        if kw['me_lc_binsize']:
            ME_LC_BINSIZE = kw['me_lc_binsize']
        else:
            ME_LC_BINSIZE = 1
        melcgen_cmd = melcgen(rawfiles, outdirs, binsize=ME_LC_BINSIZE, minE=ME_LC_EMIN, maxE=ME_LC_EMAX)
        pipeline_commands.append(melcgen_cmd)
        #mespecgen
        mespecgen_cmd = mespecgen(rawfiles, outdirs)
        pipeline_commands.append(mespecgen_cmd)
        #merspgen
        merspgen_cmd = merspgen(rawfiles, outdirs, ra=ra, dec=dec)
        # merspgen is a list
        pipeline_commands.append(merspgen_cmd)
        #mebkgmap for spec
        mebkgmap_cmd = mebkgmap(rawfiles, outdirs, flag="spec", minE=None, maxE=None)
        pipeline_commands = pipeline_commands + mebkgmap_cmd
        #mebkgmap for lc
        mebkgmap_cmd = mebkgmap(rawfiles, outdirs, flag="lc", minE=ME_LC_EMIN, maxE=ME_LC_EMAX)
        pipeline_commands = pipeline_commands + mebkgmap_cmd
        if bary_flag:
            hxbary_cmd = hxbary(rawfiles, outdirs, ra=ra, dec=dec, instrument=instrument)
            pipeline_commands.append(hxbary_cmd)
    elif instrument == "LE":
        #lepical
        lepical_cmd = lepical(rawfiles, outdirs)
        pipeline_commands.append(lepical_cmd)
        #legrade
        lerecon_cmd = lerecon(rawfiles, outdirs)
        pipeline_commands.append(lerecon_cmd)
        #legtigen
        legtigen_cmd = legtigen(rawfiles, outdirs)
        pipeline_commands = pipeline_commands + legtigen_cmd
        #lescreen
        lescreen_cmd = lescreen(rawfiles, outdirs)
        pipeline_commands.append(lescreen_cmd)
        #lelcgen
        #NOTE:2.04 update -- LC energy range selection
        if kw['le_lc_emin']:
            LE_LC_EMIN = kw['le_lc_emin']
        else:
            LE_LC_EMIN = 1
        if kw['le_lc_emax']:
            LE_LC_EMAX = kw['le_lc_emax']
        else:
            LE_LC_EMAX = 10 
        if kw['le_lc_binsize']:
            LE_LC_BINSIZE = kw['le_lc_binsize']
        else:
            LE_LC_BINSIZE = 1
        lelcgen_cmd = lelcgen(rawfiles, outdirs, binsize=LE_LC_BINSIZE, minE=LE_LC_EMIN, maxE=LE_LC_EMAX)
        pipeline_commands.append(lelcgen_cmd)
        #lespecgen
        lespecgen_cmd = lespecgen(rawfiles, outdirs)
        pipeline_commands.append(lespecgen_cmd)
        #lerspgen
        lerspgen_cmd = lerspgen(rawfiles, outdirs, ra=ra, dec=dec)
        # lerspgen is a list
        pipeline_commands.append(lerspgen_cmd)
        #lebkgmap for spec
        lebkgmap_cmd = lebkgmap(rawfiles, outdirs, flag="spec", minE=None, maxE=None)
        pipeline_commands = pipeline_commands + lebkgmap_cmd
        #lebkgmap for lc
        lebkgmap_cmd = lebkgmap(rawfiles, outdirs, flag="lc", minE=LE_LC_EMIN, maxE=LE_LC_EMAX)
        pipeline_commands = pipeline_commands + lebkgmap_cmd
        if bary_flag:
            hxbary_cmd = hxbary(rawfiles, outdirs, ra=ra, dec=dec, instrument=instrument)
            pipeline_commands.append(hxbary_cmd)
        if kw['clean_flag']:
            clean_data_cmd = clean_data(rawfiles, outdirs, version=version, parallel_flag=parallel_flag)
            pipeline_commands.append(clean_data_cmd)
    return pipeline_commands

if __name__ == "__main__":
    class bcolors:
        HEADER = '\033[95m'
        OKBLUE = '\033[94m'
        OKCYAN = '\033[96m'
        OKGREEN = '\033[92m'
        WARNING = '\033[93m'
        FAIL = '\033[91m'
        ENDC = '\033[0m'
        BOLD = '\033[1m'
        UNDERLINE = '\033[4m'

    NOTICE = """

    -------------------------------
    Notice : 
        HXMTsoft pipeline. Using this program, you can generate a shell script that 
        contains all the commands you need to complete the HXMT data processing.

    %sWarning : !!! The software is currently used to process hxmtsoft version 2.04, 
        if you need to process version 2.02 of hxmtsoft, use the --version parameter to specify the hxmtsoft version!!!%s
    -------------------------------

    """%(bcolors.WARNING, bcolors.ENDC)
    # input arguments
    #TODO:finish documentary
    parser = argparse.ArgumentParser(formatter_class=argparse.RawDescriptionHelpFormatter,
            description=NOTICE + 'Example: hpipeline -i /DATA_PATH/ExpID/ -o /OUTPUT_PATH/ --hxbary -r 83.63322083 -d 22.014461 -b bash-script-name.sh')
    parser.add_argument("-i","--input",help="data archived path")
    parser.add_argument("-I","--inputlist",help="data archived path in list",type=str)
    parser.add_argument("-o","--output",help="products archived path")
    parser.add_argument("-O","--outputlist",help="products archived path in list",type=str)
    parser.add_argument("-b","--bash",help="produce a bash script file",type=str)

    # optional 
    parser.add_argument("--hxbary",action="store_true",help="carry out Barycentric correction")
    parser.add_argument("-r","--ra",help="right ascension of barycentering correction (unit: degree)",type=float)
    parser.add_argument("-d","--dec",help="declination of barycentering correction (unit: degree)",type=float)
    parser.add_argument("-v","--version",help="the pipeline is compatible with HXMTsoft version 2.04 (default), if --version 2.02 , the pipeline is compatible with HXMTsoft v2.02", type=str)
    parser.add_argument("--LE_LC_EMIN",help="lower limits for LE lightcurve (unit: keV)",type=float)
    parser.add_argument("--LE_LC_EMAX",help="upper limits for LE lightcurve (unit: keV)",type=float)
    parser.add_argument("--LE_LC_BINSIZE",help="binsize LE lightcurve (unit: second)",type=float)
    parser.add_argument("--ME_LC_EMIN",help="lower limits for ME lightcurve (unit: keV)",type=float)
    parser.add_argument("--ME_LC_EMAX",help="upper limits for ME lightcurve (unit: keV)",type=float)
    parser.add_argument("--ME_LC_BINSIZE",help="binsize ME lightcurve (unit: second)",type=float)
    parser.add_argument("--HE_LC_EMIN",help="lower limits for HE lightcurve (unti: keV)",type=float)
    parser.add_argument("--HE_LC_EMAX",help="upper limits for HE lightcurve (unti: keV)",type=float)
    parser.add_argument("--HE_LC_BINSIZE",help="binsize HE lightcurve (unit: second)",type=float)

    parser.add_argument("-c", "--clean", action="store_true", help="delete the events file generated in process, keep screen file only (default keeps all)")
    parser.add_argument("-p", "--parallel", action="store_true", help="setup environmental variables for parallel processing")
    args = parser.parse_args()

    if args.version:
        version = args.version
    else:
        version = '2.04'

    if args.clean:
        clean_flag = True
    else:
        clean_flag = False

    if args.parallel:
        parallel_flag = True
    else:
        parallel_flag = False


    if args.inputlist:
        inputfile = open(args.inputlist)
        outputfile= open(args.outputlist)
        bashfile  = args.bash
        lines = []
        for data_dir,product_dir in zip(inputfile,outputfile):
            data_dir = data_dir[0:-1]
            product_dir = product_dir[0:-1]
            print("creating pipeline for ... ",data_dir)
            if args.hxbary:
                ra = args.ra
                dec = args.dec
                try:
                    lines = lines + main(data_dir, product_dir, ra=ra, dec=dec, instrument="HE", bary_flag=True, clean_flag=clean_flag, parallel_flag=parallel_flag, 
                            version=version, le_lc_emin=args.LE_LC_EMIN, le_lc_emax=args.LE_LC_EMAX, 
                            me_lc_emin=args.ME_LC_EMIN, me_lc_emax=args.ME_LC_EMAX,
                            he_lc_emin=args.HE_LC_EMIN, he_lc_emax=args.HE_LC_EMAX, 
                            he_lc_binsize=args.HE_LC_BINSIZE, me_lc_binsize=args.ME_LC_BINSIZE, le_lc_binsize=args.LE_LC_BINSIZE)
                    lines = lines + main(data_dir, product_dir, ra=ra, dec=dec, instrument="ME", bary_flag=True, clean_flag=clean_flag, parallel_flag=parallel_flag, 
                            version=version, le_lc_emin=args.LE_LC_EMIN, le_lc_emax=args.LE_LC_EMAX, 
                            me_lc_emin=args.ME_LC_EMIN, me_lc_emax=args.ME_LC_EMAX,
                            he_lc_emin=args.HE_LC_EMIN, he_lc_emax=args.HE_LC_EMAX,
                            he_lc_binsize=args.HE_LC_BINSIZE, me_lc_binsize=args.ME_LC_BINSIZE, le_lc_binsize=args.LE_LC_BINSIZE)
                    lines = lines + main(data_dir, product_dir, ra=ra, dec=dec, instrument="LE", bary_flag=True, clean_flag=clean_flag, parallel_flag=parallel_flag, 
                            version=version, le_lc_emin=args.LE_LC_EMIN, le_lc_emax=args.LE_LC_EMAX, 
                            me_lc_emin=args.ME_LC_EMIN, me_lc_emax=args.ME_LC_EMAX,
                            he_lc_emin=args.HE_LC_EMIN, he_lc_emax=args.HE_LC_EMAX,
                            he_lc_binsize=args.HE_LC_BINSIZE, me_lc_binsize=args.ME_LC_BINSIZE, le_lc_binsize=args.LE_LC_BINSIZE)
                except:continue
            else:
                if args.ra or args.dec:
                    try:
                        lines = lines + main(data_dir, product_dir,ra=ra, dec=dec, instrument="HE", bary_flag=False, clean_flag=clean_flag, parallel_flag=parallel_flag, 
                                version=version, le_lc_emin=args.LE_LC_EMIN, le_lc_emax=args.LE_LC_EMAX, 
                                me_lc_emin=args.ME_LC_EMIN, me_lc_emax=args.ME_LC_EMAX,
                                he_lc_emin=args.HE_LC_EMIN, he_lc_emax=args.HE_LC_EMAX,
                                he_lc_binsize=args.HE_LC_BINSIZE, me_lc_binsize=args.ME_LC_BINSIZE, le_lc_binsize=args.LE_LC_BINSIZE)
                        lines = lines + main(data_dir, product_dir,ra=ra, dec=dec, instrument="ME", bary_flag=False, clean_flag=clean_flag, parallel_flag=parallel_flag, 
                                version=version, le_lc_emin=args.LE_LC_EMIN, le_lc_emax=args.LE_LC_EMAX, 
                                me_lc_emin=args.ME_LC_EMIN, me_lc_emax=args.ME_LC_EMAX,
                                he_lc_emin=args.HE_LC_EMIN, he_lc_emax=args.HE_LC_EMAX,
                                he_lc_binsize=args.HE_LC_BINSIZE, me_lc_binsize=args.ME_LC_BINSIZE, le_lc_binsize=args.LE_LC_BINSIZE)
                        lines = lines + main(data_dir, product_dir,ra=ra, dec=dec, instrument="LE", bary_flag=False, clean_flag=clean_flag, parallel_flag=parallel_flag, 
                                version=version, le_lc_emin=args.LE_LC_EMIN, le_lc_emax=args.LE_LC_EMAX, 
                                me_lc_emin=args.ME_LC_EMIN, me_lc_emax=args.ME_LC_EMAX,
                                he_lc_emin=args.HE_LC_EMIN, he_lc_emax=args.HE_LC_EMAX,
                                he_lc_binsize=args.HE_LC_BINSIZE, me_lc_binsize=args.ME_LC_BINSIZE, le_lc_binsize=args.LE_LC_BINSIZE)
                    except:continue
                else:
                    try:
                        lines = lines + main(data_dir, product_dir, instrument="HE", bary_flag=False, clean_flag=clean_flag, parallel_flag=parallel_flag, 
                                version=version, le_lc_emin=args.LE_LC_EMIN, le_lc_emax=args.LE_LC_EMAX, 
                                me_lc_emin=args.ME_LC_EMIN, me_lc_emax=args.ME_LC_EMAX,
                                he_lc_emin=args.HE_LC_EMIN, he_lc_emax=args.HE_LC_EMAX,
                                he_lc_binsize=args.HE_LC_BINSIZE, me_lc_binsize=args.ME_LC_BINSIZE, le_lc_binsize=args.LE_LC_BINSIZE)
                        lines = lines + main(data_dir, product_dir, instrument="ME", bary_flag=False, clean_flag=clean_flag, parallel_flag=parallel_flag, 
                                version=version, le_lc_emin=args.LE_LC_EMIN, le_lc_emax=args.LE_LC_EMAX, 
                                me_lc_emin=args.ME_LC_EMIN, me_lc_emax=args.ME_LC_EMAX,
                                he_lc_emin=args.HE_LC_EMIN, he_lc_emax=args.HE_LC_EMAX,
                                he_lc_binsize=args.HE_LC_BINSIZE, me_lc_binsize=args.ME_LC_BINSIZE, le_lc_binsize=args.LE_LC_BINSIZE)
                        lines = lines + main(data_dir, product_dir, instrument="LE", bary_flag=False, clean_flag=clean_flag, parallel_flag=parallel_flag, 
                                version=version, le_lc_emin=args.LE_LC_EMIN, le_lc_emax=args.LE_LC_EMAX, 
                                me_lc_emin=args.ME_LC_EMIN, me_lc_emax=args.ME_LC_EMAX,
                                he_lc_emin=args.HE_LC_EMIN, he_lc_emax=args.HE_LC_EMAX,
                                he_lc_binsize=args.HE_LC_BINSIZE, me_lc_binsize=args.ME_LC_BINSIZE, le_lc_binsize=args.LE_LC_BINSIZE)
                    except:continue
        if args.bash:
            bashfile  = args.bash
            with open(bashfile,'w')as fout:
                for i in lines:
                    wrt_str = "%s\n"%(i)
                    fout.write(wrt_str)
                
            print('\n')
            print("     you have successfully created a pipeline script: %s"%bashfile)
            print('     Run shell command "source %s" '%bashfile)
            print('\n')
        else:
            bashfile  = ""
            for i in lines:
                print(i)

    elif args.input == None:
        print('ERROR: no inputs. "hpipeline -h" see help')
    else:
        data_dir = args.input
        product_dir = args.output
        bashfile  = args.bash
        lines = []
        if bashfile:
            bashfile  = args.bash
        else:
            bashfile  = ""
        if args.hxbary:
            ra = args.ra
            dec = args.dec
            lines = lines + main(data_dir, product_dir, ra=ra, dec=dec,instrument="HE",bary_flag=True, clean_flag=clean_flag, parallel_flag=parallel_flag,
                    version=version, le_lc_emin=args.LE_LC_EMIN, le_lc_emax=args.LE_LC_EMAX,                                  
                    me_lc_emin=args.ME_LC_EMIN, me_lc_emax=args.ME_LC_EMAX,                                                   
                    he_lc_emin=args.HE_LC_EMIN, he_lc_emax=args.HE_LC_EMAX,                                                   
                    he_lc_binsize=args.HE_LC_BINSIZE, me_lc_binsize=args.ME_LC_BINSIZE, le_lc_binsize=args.LE_LC_BINSIZE)     
            lines = lines + main(data_dir, product_dir, ra=ra, dec=dec,instrument="ME",bary_flag=True, clean_flag=clean_flag, parallel_flag=parallel_flag,
                    version=version, le_lc_emin=args.LE_LC_EMIN, le_lc_emax=args.LE_LC_EMAX,                                 
                    me_lc_emin=args.ME_LC_EMIN, me_lc_emax=args.ME_LC_EMAX,                                                  
                    he_lc_emin=args.HE_LC_EMIN, he_lc_emax=args.HE_LC_EMAX,                                                  
                    he_lc_binsize=args.HE_LC_BINSIZE, me_lc_binsize=args.ME_LC_BINSIZE, le_lc_binsize=args.LE_LC_BINSIZE)    
            lines = lines + main(data_dir, product_dir, ra=ra, dec=dec,instrument="LE",bary_flag=True, clean_flag=clean_flag, parallel_flag=parallel_flag,
                    version=version, le_lc_emin=args.LE_LC_EMIN, le_lc_emax=args.LE_LC_EMAX, 
                    me_lc_emin=args.ME_LC_EMIN, me_lc_emax=args.ME_LC_EMAX,
                    he_lc_emin=args.HE_LC_EMIN, he_lc_emax=args.HE_LC_EMAX,
                    he_lc_binsize=args.HE_LC_BINSIZE, me_lc_binsize=args.ME_LC_BINSIZE, le_lc_binsize=args.LE_LC_BINSIZE)
        elif args.ra or args.dec:
            ra = args.ra
            dec = args.dec
            lines = lines + main(data_dir, product_dir, ra=ra, dec=dec, instrument="HE",bary_flag=False, clean_flag=clean_flag, parallel_flag=parallel_flag, 
                    version=version, le_lc_emin=args.LE_LC_EMIN, le_lc_emax=args.LE_LC_EMAX, 
                    me_lc_emin=args.ME_LC_EMIN, me_lc_emax=args.ME_LC_EMAX,
                    he_lc_emin=args.HE_LC_EMIN, he_lc_emax=args.HE_LC_EMAX,
                    he_lc_binsize=args.HE_LC_BINSIZE, me_lc_binsize=args.ME_LC_BINSIZE, le_lc_binsize=args.LE_LC_BINSIZE)
            lines = lines + main(data_dir, product_dir, ra=ra, dec=dec, instrument="ME",bary_flag=False, clean_flag=clean_flag, parallel_flag=parallel_flag, 
                    version=version, le_lc_emin=args.LE_LC_EMIN, le_lc_emax=args.LE_LC_EMAX, 
                    me_lc_emin=args.ME_LC_EMIN, me_lc_emax=args.ME_LC_EMAX,
                    he_lc_emin=args.HE_LC_EMIN, he_lc_emax=args.HE_LC_EMAX,
                    he_lc_binsize=args.HE_LC_BINSIZE, me_lc_binsize=args.ME_LC_BINSIZE, le_lc_binsize=args.LE_LC_BINSIZE)
            lines = lines + main(data_dir, product_dir, ra=ra, dec=dec, instrument="LE",bary_flag=False, clean_flag=clean_flag, parallel_flag=parallel_flag, 
                    version=version, le_lc_emin=args.LE_LC_EMIN, le_lc_emax=args.LE_LC_EMAX, 
                    me_lc_emin=args.ME_LC_EMIN, me_lc_emax=args.ME_LC_EMAX,
                    he_lc_emin=args.HE_LC_EMIN, he_lc_emax=args.HE_LC_EMAX,
                    he_lc_binsize=args.HE_LC_BINSIZE, me_lc_binsize=args.ME_LC_BINSIZE, le_lc_binsize=args.LE_LC_BINSIZE)
        else:
            lines = lines + main(data_dir, product_dir, instrument="HE", bary_flag=False, clean_flag=clean_flag, parallel_flag=parallel_flag, 
                    version=version, le_lc_emin=args.LE_LC_EMIN, le_lc_emax=args.LE_LC_EMAX, 
                    me_lc_emin=args.ME_LC_EMIN, me_lc_emax=args.ME_LC_EMAX,
                    he_lc_emin=args.HE_LC_EMIN, he_lc_emax=args.HE_LC_EMAX,
                    he_lc_binsize=args.HE_LC_BINSIZE, me_lc_binsize=args.ME_LC_BINSIZE, le_lc_binsize=args.LE_LC_BINSIZE)
            lines = lines + main(data_dir, product_dir, instrument="ME", bary_flag=False, clean_flag=clean_flag, parallel_flag=parallel_flag, 
                    version=version, le_lc_emin=args.LE_LC_EMIN, le_lc_emax=args.LE_LC_EMAX, 
                    me_lc_emin=args.ME_LC_EMIN, me_lc_emax=args.ME_LC_EMAX,
                    he_lc_emin=args.HE_LC_EMIN, he_lc_emax=args.HE_LC_EMAX,
                    he_lc_binsize=args.HE_LC_BINSIZE, me_lc_binsize=args.ME_LC_BINSIZE, le_lc_binsize=args.LE_LC_BINSIZE)
            lines = lines + main(data_dir, product_dir, instrument="LE", bary_flag=False, clean_flag=clean_flag, parallel_flag=parallel_flag, 
                    version=version, le_lc_emin=args.LE_LC_EMIN, le_lc_emax=args.LE_LC_EMAX, 
                    me_lc_emin=args.ME_LC_EMIN, me_lc_emax=args.ME_LC_EMAX,
                    he_lc_emin=args.HE_LC_EMIN, he_lc_emax=args.HE_LC_EMAX,
                    he_lc_binsize=args.HE_LC_BINSIZE, me_lc_binsize=args.ME_LC_BINSIZE, le_lc_binsize=args.LE_LC_BINSIZE)

        if bashfile == "":
            for i in lines:
                print(i)
        else:
            with open(bashfile,'w')as fout:
                for i in lines:
                    wrt_str = "%s\n"%(i)
                    fout.write(wrt_str)
            print('\n')
            print("     you have successfully created a pipeline script: %s"%bashfile)
            print('     Run shell command "source %s" '%bashfile)
            print('\n')
