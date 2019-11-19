#!/usr/bin/env python
##################################
'''
HXMT pipeline, run python hpipeline.py -h for help.

NOTE: this script is suitable for HXMTDAS v2.01,
check out "http://code.ihep.ac.cn/tuoyl/hxmt_pipeline" for details.
'''
import argparse
import os
import sys
import glob
from astropy.io import fits

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

class pipelineError(Exception):
    pass

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
    hepical_cmd = 'hepical evtfile="%s" outfile="%s" clobber=yes'%(evtfile, outfile)
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
    'ehkfile="%s" defaultexpr=NONE expr="ELV>10&&COR>8&&TN_SAA>300&&T_SAA>300&&ANG_DIST<=0.04" '\
    'pmexpr="" clobber=yes history=yes'%(hvfile, tempfile, pmfile, outfile, ehkfile)
    return hegtigen_cmd

def megtigen(data_dict, dir_dict):
    megtigen_cmd = []
    tempfile = data_dict["TH"]
    ehkfile = data_dict["EHK"]
    prefix = get_expID(data_dict)
    outfile = os.path.join(dir_dict["tmp"], prefix+"_ME_gti.fits")
    megtigen_cmd.append('megtigen tempfile="%s" ehkfile="%s" outfile="%s" '\
            'defaultexpr=NONE expr="ELV>10&&COR>8&&T_SAA>300&&TN_SAA>300&&ANG_DIST<=0.04" '\
            'clobber=yes history=yes'%(tempfile, ehkfile, outfile))
    #new le gti
    gradefile  = os.path.join(dir_dict["tmp"], prefix+"_ME_grade.fits")
    baddetector= "$HEADAS/refdata/medetectorstatus.fits"
    newstatus  = os.path.join(dir_dict["tmp"], prefix+"_ME_status.fits")
    newgti_cmd = 'megti %s %s %s %s %s'%(gradefile, outfile, outfile, baddetector, newstatus)
    megtigen_cmd.append(newgti_cmd)
    return megtigen_cmd

def legtigen(data_dict, dir_dict):
    legtigen_cmd = []
    eventfile= data_dict["Evt"]
    tempfile = data_dict["TH"]
    ehkfile = data_dict["EHK"]
    instatfile = data_dict["InsStat"]
    prefix = get_expID(data_dict)
    outfile = os.path.join(dir_dict["tmp"], prefix+"_LE_gti.fits")
    legtigen_cmd.append('legtigen evtfile="%s" instatusfile="%s" tempfile="%s" ehkfile="%s" '\
            'outfile="%s" defaultexpr=NONE expr="ELV>10&&DYE_ELV>30&&COR>8&&T_SAA>=300&&TN_SAA>=300&&ANG_DIST<=0.04" '\
            'clobber=yes history=yes'%("", instatfile, tempfile, ehkfile, outfile))
    #new le gti
    reconfile = os.path.join(dir_dict["tmp"], prefix+"_LE_recon.fits")
    newgti_cmd = 'legti %s %s %s'%(reconfile, outfile, outfile)
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

def helcgen(data_dict, dir_dict, binsize=1, minPI=25, maxPI=100):
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

def melcgen(data_dict, dir_dict, binsize=1, minPI=25, maxPI=100):
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

def lelcgen(data_dict, dir_dict, binsize=1, minPI=25, maxPI=100):
    prefix = get_expID(data_dict)
    screenfile  = os.path.join(dir_dict["clean"], prefix+"_LE_screen.fits")
    outfile     = os.path.join(dir_dict["lightcurves"], prefix+"_LE_lc")
    userdetid   = "0,2-4,6-10,12,14,20,22-26,28,30,32,34-36,38-42,44,46,52,54-58,60-62,64,66-68,70-74,76,78,84,86,88-90,92-94"
    lelcgen_cmd = 'lelcgen evtfile="%s" outfile="%s" '\
            'userdetid="%s" binsize=%s starttime=0 stoptime=0 '\
            'minPI=%s maxPI=%s eventtype=1 clobber=yes'%(
                    screenfile, outfile, userdetid, str(binsize), str(minPI), str(maxPI))
    return lelcgen_cmd

def hespecgen(data_dict, dir_dict):
    prefix = get_expID(data_dict)
    screenfile  = os.path.join(dir_dict["clean"], prefix+"_HE_screen.fits")
    outfile     = os.path.join(dir_dict["spectra"], prefix+"_HE_spec")
    deadfile    = data_dict["DTime"]
    hespecgen_cmd = 'hespecgen evtfile="%s" outfile="%s" '\
            'deadfile="%s" userdetid='\
            '"0;1;2;3;4;5;6;7;8;9;10;11;12;13;14;15;16;17" eventtype=1 starttime=0 '\
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



def herspgen(data_dict, dir_dict, ra=-1, dec=-91):
    herspgen_cmd = []
    prefix = get_expID(data_dict)
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
        rsp_cmd = "herspgen %s %s %s %s %s clobber=yes"%(phafile, outfile, attfile, str(ra), str(dec))
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
    merspgen_cmd = "merspgen %s %s %s %s %s clobber=yes"%(phafile, outfile, attfile, str(ra), str(dec))
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
    lerspgen_cmd = "lerspgen %s %s %s %s %s %s clobber=yes"%(phafile, outfile, attfile, tempfile, str(ra), str(dec))
    return lerspgen_cmd

def hebkgmap(data_dict, dir_dict, flag='lc', minPI=25, maxPI=100):
    hebkgmap_cmd = []
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
        specfile = os.path.join(dir_dict["spectra"], prefix+"_HE_spec_g*.pha")
        listfile = os.path.join(dir_dict["spectra"], prefix+"_HE_spec.txt")
        create_bkglist_cmd = "ls %s | sort -V > %s"%(specfile,listfile)
        hebkgmap_cmd.append(create_bkglist_cmd)
        outfile = os.path.join(dir_dict["spectra"], prefix+"_HE_specbkg")
        hebkgmap_cmd.append('hebkgmap spec %s %s %s %s %s %s %s %s'%(screenfile, ehkfile, gtifile,
                deadfile, listfile, str(minPI), str(maxPI), outfile))
    return hebkgmap_cmd

def mebkgmap(data_dict, dir_dict, flag='lc', minPI=25, maxPI=100):
    mebkgmap_cmd = []
    prefix = get_expID(data_dict)
    screenfile  = os.path.join(dir_dict["clean"], prefix+"_ME_screen.fits")
    ehkfile = data_dict["EHK"]
    gtifile = os.path.join(dir_dict["tmp"], prefix+"_ME_gti.fits")
    deadfile = os.path.join(dir_dict["tmp"],prefix+"_ME_dtime.fits")
    tempfile = data_dict["TH"]
    if flag == 'lc':
        lcfile = os.path.join(dir_dict["lightcurves"], prefix+"_ME_lc_*.lc")
        listfile = os.path.join(dir_dict["lightcurves"], prefix+"_ME_lc.txt")
        create_bkglist_cmd = "ls %s | sort -V > %s"%(lcfile,listfile)
        mebkgmap_cmd.append(create_bkglist_cmd)
        outfile = os.path.join(dir_dict["lightcurves"], prefix+"_ME_lcbkg")
        mebkgmap_cmd.append('mebkgmap lc %s %s %s %s %s %s %s %s %s'%(
                    screenfile, ehkfile, gtifile, deadfile, tempfile, listfile, str(minPI), str(maxPI), outfile))
    if flag == 'spec':
        specfile = os.path.join(dir_dict["spectra"], prefix+"_ME_spec_*.pha")
        listfile = os.path.join(dir_dict["spectra"], prefix+"_ME_spec.txt")
        create_bkglist_cmd = "ls %s | sort -V > %s"%(specfile,listfile)
        mebkgmap_cmd.append(create_bkglist_cmd)
        outfile = os.path.join(dir_dict["spectra"], prefix+"_ME_specbkg")
        mebkgmap_cmd.append('mebkgmap spec %s %s %s %s %s %s %s %s %s'%(
                    screenfile, ehkfile, gtifile, deadfile, tempfile, listfile, str(minPI), str(maxPI), outfile))
    return mebkgmap_cmd

def lebkgmap(data_dict, dir_dict, flag='lc', minPI=25, maxPI=100):
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

def get_expID(data_dict):
    #get the Exposure ID and assign as prefix for files
    evtfile = data_dict["Evt"]
    hdulist = fits.open(evtfile)
    exp_id = hdulist[1].header["EXP_ID"]
    exp_id = exp_id.split('-')
    exp_id = exp_id[0]
    return exp_id

def main(data_dir, product_dir, instrument="HE", ra=-1, dec=-91, bary_flag=False):
    # read raw data
    rawfiles = get_rawdata(data_dir,instrument=instrument)
    outdirs  = get_dir(product_dir, instrument=instrument)

    pipeline_commands = []
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
        helcgen_cmd = helcgen(rawfiles, outdirs, minPI=26, maxPI=120)
        pipeline_commands.append(helcgen_cmd)
        #hespecgen
        hespecgen_cmd = hespecgen(rawfiles, outdirs)
        pipeline_commands.append(hespecgen_cmd)
        #herspgen
        herspgen_cmd = herspgen(rawfiles, outdirs, ra=ra, dec=dec)
        # herspgen is a list
        pipeline_commands = pipeline_commands + herspgen_cmd
        #hebkgmap for spec
        hebkgmap_cmd = hebkgmap(rawfiles, outdirs, flag="spec", minPI=0, maxPI=255)
        pipeline_commands = pipeline_commands + hebkgmap_cmd
        #hebkgmap for lc
        hebkgmap_cmd = hebkgmap(rawfiles, outdirs, flag="lc", minPI=26, maxPI=120)
        pipeline_commands = pipeline_commands + hebkgmap_cmd
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
        melcgen_cmd = melcgen(rawfiles, outdirs, minPI=120, maxPI=290)
        pipeline_commands.append(melcgen_cmd)
        #mespecgen
        mespecgen_cmd = mespecgen(rawfiles, outdirs)
        pipeline_commands.append(mespecgen_cmd)
        #merspgen
        merspgen_cmd = merspgen(rawfiles, outdirs, ra=ra, dec=dec)
        # merspgen is a list
        pipeline_commands.append(merspgen_cmd)
        #mebkgmap for spec
        mebkgmap_cmd = mebkgmap(rawfiles, outdirs, flag="spec", minPI=0, maxPI=1023)
        pipeline_commands = pipeline_commands + mebkgmap_cmd
        #mebkgmap for lc
        mebkgmap_cmd = mebkgmap(rawfiles, outdirs, flag="lc", minPI=120, maxPI=290)
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
        lelcgen_cmd = lelcgen(rawfiles, outdirs, minPI=106, maxPI=1170)
        pipeline_commands.append(lelcgen_cmd)
        #lespecgen
        lespecgen_cmd = lespecgen(rawfiles, outdirs)
        pipeline_commands.append(lespecgen_cmd)
        #lerspgen
        lerspgen_cmd = lerspgen(rawfiles, outdirs, ra=ra, dec=dec)
        # lerspgen is a list
        pipeline_commands.append(lerspgen_cmd)
        #lebkgmap for spec
        lebkgmap_cmd = lebkgmap(rawfiles, outdirs, flag="spec", minPI=0, maxPI=1535)
        pipeline_commands = pipeline_commands + lebkgmap_cmd
        #lebkgmap for lc
        lebkgmap_cmd = lebkgmap(rawfiles, outdirs, flag="lc", minPI=106, maxPI=1170)
        pipeline_commands = pipeline_commands + lebkgmap_cmd
        if bary_flag:
            hxbary_cmd = hxbary(rawfiles, outdirs, ra=ra, dec=dec, instrument=instrument)
            pipeline_commands.append(hxbary_cmd)
    return pipeline_commands

if __name__ == "__main__":
    # input arguments
    #TODO:finish documentary
    parser = argparse.ArgumentParser(formatter_class=argparse.RawDescriptionHelpFormatter,
            description='Example: python he_pipeline.py -i /DATA_PATH/ExpID/ -o /OUTPUT_PATH/ --hxbary -r 83.63322083 -d 22.014461 -b bash-script-name.sh')
    parser.add_argument("-i","--input",help="data archived path")
    parser.add_argument("-I","--inputlist",help="data archived path in list",type=str)
    parser.add_argument("-o","--output",help="products archived path")
    parser.add_argument("-O","--outputlist",help="products archived path in list",type=str)
    parser.add_argument("-b","--bash",help="produce a bash script file",type=str)
    parser.add_argument("--hxbary",action="store_true",help="carry out Barycentric correction")
    parser.add_argument("-r","--ra",help="right ascension of barycentering correction",type=float)
    parser.add_argument("-d","--dec",help="declination of barycentering correction",type=float)
    args = parser.parse_args()

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
                    lines = lines + main(data_dir, product_dir, ra=ra, dec=dec, instrument="HE", bary_flag=True)
                    lines = lines + main(data_dir, product_dir, ra=ra, dec=dec, instrument="ME", bary_flag=True)
                    lines = lines + main(data_dir, product_dir, ra=ra, dec=dec, instrument="LE", bary_flag=True)
                except:continue
            else:
                if args.ra or args.dec:
                    try:
                        lines = lines + main(data_dir, product_dir,ra=ra, dec=dec, instrument="HE", bary_flag=False)
                        lines = lines + main(data_dir, product_dir,ra=ra, dec=dec, instrument="ME", bary_flag=False)
                        lines = lines + main(data_dir, product_dir,ra=ra, dec=dec, instrument="LE", bary_flag=False)
                    except:continue
                else:
                    try:
                        lines = lines + main(data_dir, product_dir, instrument="HE", bary_flag=False)
                        lines = lines + main(data_dir, product_dir, instrument="ME", bary_flag=False)
                        lines = lines + main(data_dir, product_dir, instrument="LE", bary_flag=False)
                    except:continue
        if args.bash:
            bashfile  = args.bash
            with open(bashfile,'w')as fout:
                for i in lines:
                    wrt_str = "%s\n"%(i)
                    fout.write(wrt_str)
            print('\n')
            print("     you have successfully created a pipeline script: %s"%bashfile)
            print('     Run shell command ". %s" '%bashfile)
            print('\n')
        else:
            bashfile  = ""
            for i in lines:
                print(i)

    elif args.input == None:
        print('ERROR: no inputs. "python he_pipeline.py -h" see help')
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
            lines = lines + main(data_dir, product_dir, ra=ra, dec=dec,instrument="HE",bary_flag=True)
            lines = lines + main(data_dir, product_dir, ra=ra, dec=dec,instrument="ME",bary_flag=True)
            lines = lines + main(data_dir, product_dir, ra=ra, dec=dec,instrument="LE",bary_flag=True)
        elif args.ra or args.dec:
            ra = args.ra
            dec = args.dec
            lines = lines + main(data_dir, product_dir, ra=ra, dec=dec, instrument="HE",bary_flag=False)
            lines = lines + main(data_dir, product_dir, ra=ra, dec=dec, instrument="ME",bary_flag=False)
            lines = lines + main(data_dir, product_dir, ra=ra, dec=dec, instrument="LE",bary_flag=False)
        else:
            lines = lines + main(data_dir, product_dir, instrument="HE", bary_flag=False)
            lines = lines + main(data_dir, product_dir, instrument="ME", bary_flag=False)
            lines = lines + main(data_dir, product_dir, instrument="LE", bary_flag=False)

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
            print('     Run shell command ". %s" '%bashfile)
            print('\n')
