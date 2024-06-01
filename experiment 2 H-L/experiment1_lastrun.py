#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2023.1.3),
    on 五月 08, 2024, at 10:21
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

# --- Import packages ---
from psychopy import locale_setup
from psychopy import prefs
from psychopy import plugins
plugins.activatePlugins()
prefs.hardware['audioLib'] = 'ptb'
prefs.hardware['audioLatencyMode'] = '3'
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout
from psychopy.tools import environmenttools
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

import psychopy.iohub as io
from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)
# Store info about the experiment session
psychopyVersion = '2023.1.3'
expName = 'experiment1'  # from the Builder filename that created this script
expInfo = {
    'participant': '',
    'session': '001',
    'age': '',
    'gender': ['男','女'],
}
# --- Show participant info dialog --
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='C:\\Users\\Lenovo\\Desktop\\研究一实验材料\\experiment 1\\experiment1_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# --- Setup the Window ---
win = visual.Window(
    size=[1707, 1067], fullscr=True, screen=0, 
    winType='pyglet', allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    backgroundImage='background_image.jpg', backgroundFit='cover',
    blendMode='avg', useFBO=True, 
    units='height')
win.mouseVisible = False
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess
# --- Setup input devices ---
ioConfig = {}

# Setup iohub keyboard
ioConfig['Keyboard'] = dict(use_keymap='psychopy')

ioSession = '1'
if 'session' in expInfo:
    ioSession = str(expInfo['session'])
ioServer = io.launchHubServer(window=win, **ioConfig)
eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard(backend='iohub')

# --- Initialize components for Routine "intro" ---
intro_image = visual.ImageStim(
    win=win,
    name='intro_image', 
    image='intro_image.jpg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(1.1,0.8),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=512.0, interpolate=True, depth=0.0)
intro_key_resp = keyboard.Keyboard()

# --- Initialize components for Routine "intro_2" ---
intro_image2 = visual.ImageStim(
    win=win,
    name='intro_image2', 
    image='intro_image2.jpg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(1.1, 0.8),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
intro_2key_resp = keyboard.Keyboard()

# --- Initialize components for Routine "instruction_prac" ---
instruction_prac_image = visual.ImageStim(
    win=win,
    name='instruction_prac_image', 
    image='intro_prac_image.jpg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(1.1,0.8),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
instruction_prac_key_resp = keyboard.Keyboard()
# Run 'Begin Experiment' code from instruction_prac_code
safe_account =float('%.2f'%0)

# --- Initialize components for Routine "charge" ---
charge_slider = visual.Slider(win=win, name='charge_slider',
    startValue=1, size=(1.0, 0.1), pos=(0, -0.2), units=win.units,
    labels=(1,100), ticks=(1, 100), granularity=1.0,
    style='rating', styleTweaks=('triangleMarker',), opacity=None,
    labelColor='LightGray', markerColor='blue', lineColor='black', colorSpace='rgb',
    font='Open Sans', labelHeight=0.05,
    flip=False, ori=0.0, depth=-1, readOnly=False)
charge_image = visual.ImageStim(
    win=win,
    name='charge_image', 
    image='default.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0.1), size=(0.95, 0.4),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
account_text = visual.TextStim(win=win, name='account_text',
    text='',
    font='Open Sans',
    pos=(-0.45, 0.37), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
charge_button = visual.ButtonStim(win, 
    text='', font='Arvo',
    pos=(0, -0.35),
    letterHeight=0.05,
    size=(0.3, 0.1), borderWidth=0.0,
    fillColor=[0.9216, 0.9216, 0.7255], borderColor=None,
    color='black', colorSpace='rgb',
    opacity=None,
    bold=True, italic=False,
    padding=None,
    anchor='center',
    name='charge_button',
    depth=-4
)
charge_button.buttonClock = core.Clock()

# --- Initialize components for Routine "trial" ---
# Run 'Begin Experiment' code from trial_code
initSize = 0.08
expandSize = 0.002
balloonSize=0.08

safe_account  =float("{:.2f}".format(0))

tri_num = 0
Balloon = visual.ImageStim(
    win=win,
    name='Balloon', units='norm', 
    image='default.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
reminder_text = visual.TextStim(win=win, name='reminder_text',
    text='',
    font='Times New Roman',
    units='height', pos=(0, 0.37), height=0.04, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
safeaccount_text = visual.TextStim(win=win, name='safeaccount_text',
    text='',
    font='Open Sans',
    pos=(-0.45, 0.37), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
investaccount_text = visual.TextStim(win=win, name='investaccount_text',
    text='',
    font='Open Sans',
    pos=(0.45, 0.37), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);
bankButton_key_resp = keyboard.Keyboard()
pumpwarning_text = visual.TextStim(win=win, name='pumpwarning_text',
    text='',
    font='Open Sans',
    pos=(0, -0.3), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-6.0);
text = visual.TextStim(win=win, name='text',
    text='',
    font='Open Sans',
    pos=(0, 0.3), height=0.03, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-7.0);

# --- Initialize components for Routine "feedback" ---
# Run 'Begin Experiment' code from feedback_code
from psychopy import sound
feedbackText=''
bang = sound.Sound("bang.wav")
leaky = sound.Sound("leaky.wav") #TODO


feedback_image = visual.ImageStim(
    win=win,
    name='feedback_image', 
    image='default.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0.1), size=(0.15, 0.22),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
feedback_text = visual.TextStim(win=win, name='feedback_text',
    text='',
    font='Open Sans',
    pos=(0, -0.2), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
feedback_key_resp = keyboard.Keyboard()

# --- Initialize components for Routine "assessment" ---
assessment_text = visual.TextStim(win=win, name='assessment_text',
    text='',
    font='Open Sans',
    pos=(0, 0.1), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
assessment_image = visual.ImageStim(
    win=win,
    name='assessment_image', 
    image='default.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0.05), size=(1, 0.4),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
assessment_slider = visual.Slider(win=win, name='assessment_slider',
    startValue=None, size=(1.0, 0.1), pos=(0, -0.2), units=win.units,
    labels=(1, 2, 3, 4, 5, 6, 7), ticks=(1, 2, 3, 4, 5, 6, 7), granularity=1.0,
    style='rating', styleTweaks=('labels45',), opacity=None,
    labelColor='black', markerColor='black', lineColor='black', colorSpace='rgb',
    font='Open Sans', labelHeight=0.05,
    flip=False, ori=0.0, depth=-2, readOnly=False)

# --- Initialize components for Routine "earned" ---
earned_text = visual.TextStim(win=win, name='earned_text',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
earned_key_resp = keyboard.Keyboard()

# --- Initialize components for Routine "instructions" ---
formal_image = visual.ImageStim(
    win=win,
    name='formal_image', 
    image='formal_image.jpg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(1.1, 0.85),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
instructions_key_resp = keyboard.Keyboard()

# --- Initialize components for Routine "charge" ---
charge_slider = visual.Slider(win=win, name='charge_slider',
    startValue=1, size=(1.0, 0.1), pos=(0, -0.2), units=win.units,
    labels=(1,100), ticks=(1, 100), granularity=1.0,
    style='rating', styleTweaks=('triangleMarker',), opacity=None,
    labelColor='LightGray', markerColor='blue', lineColor='black', colorSpace='rgb',
    font='Open Sans', labelHeight=0.05,
    flip=False, ori=0.0, depth=-1, readOnly=False)
charge_image = visual.ImageStim(
    win=win,
    name='charge_image', 
    image='default.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0.1), size=(0.95, 0.4),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
account_text = visual.TextStim(win=win, name='account_text',
    text='',
    font='Open Sans',
    pos=(-0.45, 0.37), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
charge_button = visual.ButtonStim(win, 
    text='', font='Arvo',
    pos=(0, -0.35),
    letterHeight=0.05,
    size=(0.3, 0.1), borderWidth=0.0,
    fillColor=[0.9216, 0.9216, 0.7255], borderColor=None,
    color='black', colorSpace='rgb',
    opacity=None,
    bold=True, italic=False,
    padding=None,
    anchor='center',
    name='charge_button',
    depth=-4
)
charge_button.buttonClock = core.Clock()

# --- Initialize components for Routine "trial" ---
# Run 'Begin Experiment' code from trial_code
initSize = 0.08
expandSize = 0.002
balloonSize=0.08

safe_account  =float("{:.2f}".format(0))

tri_num = 0
Balloon = visual.ImageStim(
    win=win,
    name='Balloon', units='norm', 
    image='default.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
reminder_text = visual.TextStim(win=win, name='reminder_text',
    text='',
    font='Times New Roman',
    units='height', pos=(0, 0.37), height=0.04, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
safeaccount_text = visual.TextStim(win=win, name='safeaccount_text',
    text='',
    font='Open Sans',
    pos=(-0.45, 0.37), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
investaccount_text = visual.TextStim(win=win, name='investaccount_text',
    text='',
    font='Open Sans',
    pos=(0.45, 0.37), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);
bankButton_key_resp = keyboard.Keyboard()
pumpwarning_text = visual.TextStim(win=win, name='pumpwarning_text',
    text='',
    font='Open Sans',
    pos=(0, -0.3), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-6.0);
text = visual.TextStim(win=win, name='text',
    text='',
    font='Open Sans',
    pos=(0, 0.3), height=0.03, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-7.0);

# --- Initialize components for Routine "feedback" ---
# Run 'Begin Experiment' code from feedback_code
from psychopy import sound
feedbackText=''
bang = sound.Sound("bang.wav")
leaky = sound.Sound("leaky.wav") #TODO


feedback_image = visual.ImageStim(
    win=win,
    name='feedback_image', 
    image='default.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0.1), size=(0.15, 0.22),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
feedback_text = visual.TextStim(win=win, name='feedback_text',
    text='',
    font='Open Sans',
    pos=(0, -0.2), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
feedback_key_resp = keyboard.Keyboard()

# --- Initialize components for Routine "assessment" ---
assessment_text = visual.TextStim(win=win, name='assessment_text',
    text='',
    font='Open Sans',
    pos=(0, 0.1), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
assessment_image = visual.ImageStim(
    win=win,
    name='assessment_image', 
    image='default.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0.05), size=(1, 0.4),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
assessment_slider = visual.Slider(win=win, name='assessment_slider',
    startValue=None, size=(1.0, 0.1), pos=(0, -0.2), units=win.units,
    labels=(1, 2, 3, 4, 5, 6, 7), ticks=(1, 2, 3, 4, 5, 6, 7), granularity=1.0,
    style='rating', styleTweaks=('labels45',), opacity=None,
    labelColor='black', markerColor='black', lineColor='black', colorSpace='rgb',
    font='Open Sans', labelHeight=0.05,
    flip=False, ori=0.0, depth=-2, readOnly=False)

# --- Initialize components for Routine "earned" ---
earned_text = visual.TextStim(win=win, name='earned_text',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
earned_key_resp = keyboard.Keyboard()

# --- Initialize components for Routine "ending" ---
ending_text = visual.TextStim(win=win, name='ending_text',
    text='    实验结束\n请按“空格键”退出',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
ending_key_resp = keyboard.Keyboard()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.Clock()  # to track time remaining of each (possibly non-slip) routine 

# --- Prepare to start Routine "intro" ---
continueRoutine = True
# update component parameters for each repeat
intro_key_resp.keys = []
intro_key_resp.rt = []
_intro_key_resp_allKeys = []
# keep track of which components have finished
introComponents = [intro_image, intro_key_resp]
for thisComponent in introComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "intro" ---
routineForceEnded = not continueRoutine
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *intro_image* updates
    
    # if intro_image is starting this frame...
    if intro_image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        intro_image.frameNStart = frameN  # exact frame index
        intro_image.tStart = t  # local t and not account for scr refresh
        intro_image.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(intro_image, 'tStartRefresh')  # time at next scr refresh
        # update status
        intro_image.status = STARTED
        intro_image.setAutoDraw(True)
    
    # if intro_image is active this frame...
    if intro_image.status == STARTED:
        # update params
        pass
    
    # *intro_key_resp* updates
    waitOnFlip = False
    
    # if intro_key_resp is starting this frame...
    if intro_key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        intro_key_resp.frameNStart = frameN  # exact frame index
        intro_key_resp.tStart = t  # local t and not account for scr refresh
        intro_key_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(intro_key_resp, 'tStartRefresh')  # time at next scr refresh
        # update status
        intro_key_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(intro_key_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(intro_key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if intro_key_resp.status == STARTED and not waitOnFlip:
        theseKeys = intro_key_resp.getKeys(keyList=['space'], waitRelease=False)
        _intro_key_resp_allKeys.extend(theseKeys)
        if len(_intro_key_resp_allKeys):
            intro_key_resp.keys = _intro_key_resp_allKeys[-1].name  # just the last key pressed
            intro_key_resp.rt = _intro_key_resp_allKeys[-1].rt
            intro_key_resp.duration = _intro_key_resp_allKeys[-1].duration
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
        if eyetracker:
            eyetracker.setConnectionState(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in introComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "intro" ---
for thisComponent in introComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if intro_key_resp.keys in ['', [], None]:  # No response was made
    intro_key_resp.keys = None
thisExp.addData('intro_key_resp.keys',intro_key_resp.keys)
if intro_key_resp.keys != None:  # we had a response
    thisExp.addData('intro_key_resp.rt', intro_key_resp.rt)
    thisExp.addData('intro_key_resp.duration', intro_key_resp.duration)
thisExp.nextEntry()
# the Routine "intro" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "intro_2" ---
continueRoutine = True
# update component parameters for each repeat
intro_2key_resp.keys = []
intro_2key_resp.rt = []
_intro_2key_resp_allKeys = []
# keep track of which components have finished
intro_2Components = [intro_image2, intro_2key_resp]
for thisComponent in intro_2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "intro_2" ---
routineForceEnded = not continueRoutine
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *intro_image2* updates
    
    # if intro_image2 is starting this frame...
    if intro_image2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        intro_image2.frameNStart = frameN  # exact frame index
        intro_image2.tStart = t  # local t and not account for scr refresh
        intro_image2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(intro_image2, 'tStartRefresh')  # time at next scr refresh
        # update status
        intro_image2.status = STARTED
        intro_image2.setAutoDraw(True)
    
    # if intro_image2 is active this frame...
    if intro_image2.status == STARTED:
        # update params
        pass
    
    # *intro_2key_resp* updates
    waitOnFlip = False
    
    # if intro_2key_resp is starting this frame...
    if intro_2key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        intro_2key_resp.frameNStart = frameN  # exact frame index
        intro_2key_resp.tStart = t  # local t and not account for scr refresh
        intro_2key_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(intro_2key_resp, 'tStartRefresh')  # time at next scr refresh
        # update status
        intro_2key_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(intro_2key_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(intro_2key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if intro_2key_resp.status == STARTED and not waitOnFlip:
        theseKeys = intro_2key_resp.getKeys(keyList=['space'], waitRelease=False)
        _intro_2key_resp_allKeys.extend(theseKeys)
        if len(_intro_2key_resp_allKeys):
            intro_2key_resp.keys = _intro_2key_resp_allKeys[-1].name  # just the last key pressed
            intro_2key_resp.rt = _intro_2key_resp_allKeys[-1].rt
            intro_2key_resp.duration = _intro_2key_resp_allKeys[-1].duration
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
        if eyetracker:
            eyetracker.setConnectionState(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in intro_2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "intro_2" ---
for thisComponent in intro_2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if intro_2key_resp.keys in ['', [], None]:  # No response was made
    intro_2key_resp.keys = None
thisExp.addData('intro_2key_resp.keys',intro_2key_resp.keys)
if intro_2key_resp.keys != None:  # we had a response
    thisExp.addData('intro_2key_resp.rt', intro_2key_resp.rt)
    thisExp.addData('intro_2key_resp.duration', intro_2key_resp.duration)
thisExp.nextEntry()
# the Routine "intro_2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "instruction_prac" ---
continueRoutine = True
# update component parameters for each repeat
instruction_prac_key_resp.keys = []
instruction_prac_key_resp.rt = []
_instruction_prac_key_resp_allKeys = []
# keep track of which components have finished
instruction_pracComponents = [instruction_prac_image, instruction_prac_key_resp]
for thisComponent in instruction_pracComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "instruction_prac" ---
routineForceEnded = not continueRoutine
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instruction_prac_image* updates
    
    # if instruction_prac_image is starting this frame...
    if instruction_prac_image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instruction_prac_image.frameNStart = frameN  # exact frame index
        instruction_prac_image.tStart = t  # local t and not account for scr refresh
        instruction_prac_image.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instruction_prac_image, 'tStartRefresh')  # time at next scr refresh
        # update status
        instruction_prac_image.status = STARTED
        instruction_prac_image.setAutoDraw(True)
    
    # if instruction_prac_image is active this frame...
    if instruction_prac_image.status == STARTED:
        # update params
        pass
    
    # *instruction_prac_key_resp* updates
    waitOnFlip = False
    
    # if instruction_prac_key_resp is starting this frame...
    if instruction_prac_key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instruction_prac_key_resp.frameNStart = frameN  # exact frame index
        instruction_prac_key_resp.tStart = t  # local t and not account for scr refresh
        instruction_prac_key_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instruction_prac_key_resp, 'tStartRefresh')  # time at next scr refresh
        # update status
        instruction_prac_key_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(instruction_prac_key_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(instruction_prac_key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if instruction_prac_key_resp.status == STARTED and not waitOnFlip:
        theseKeys = instruction_prac_key_resp.getKeys(keyList=['space'], waitRelease=False)
        _instruction_prac_key_resp_allKeys.extend(theseKeys)
        if len(_instruction_prac_key_resp_allKeys):
            instruction_prac_key_resp.keys = _instruction_prac_key_resp_allKeys[-1].name  # just the last key pressed
            instruction_prac_key_resp.rt = _instruction_prac_key_resp_allKeys[-1].rt
            instruction_prac_key_resp.duration = _instruction_prac_key_resp_allKeys[-1].duration
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
        if eyetracker:
            eyetracker.setConnectionState(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instruction_pracComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "instruction_prac" ---
for thisComponent in instruction_pracComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if instruction_prac_key_resp.keys in ['', [], None]:  # No response was made
    instruction_prac_key_resp.keys = None
thisExp.addData('instruction_prac_key_resp.keys',instruction_prac_key_resp.keys)
if instruction_prac_key_resp.keys != None:  # we had a response
    thisExp.addData('instruction_prac_key_resp.rt', instruction_prac_key_resp.rt)
    thisExp.addData('instruction_prac_key_resp.duration', instruction_prac_key_resp.duration)
thisExp.nextEntry()
# the Routine "instruction_prac" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
prac_trials = data.TrialHandler(nReps=1.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('exp_condi_pra.xlsx'),
    seed=None, name='prac_trials')
thisExp.addLoop(prac_trials)  # add the loop to the experiment
thisPrac_trial = prac_trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisPrac_trial.rgb)
if thisPrac_trial != None:
    for paramName in thisPrac_trial:
        exec('{} = thisPrac_trial[paramName]'.format(paramName))

for thisPrac_trial in prac_trials:
    currentLoop = prac_trials
    # abbreviate parameter names if possible (e.g. rgb = thisPrac_trial.rgb)
    if thisPrac_trial != None:
        for paramName in thisPrac_trial:
            exec('{} = thisPrac_trial[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "charge" ---
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from charge_code
    tmp_invest =1
    safe_account_text = '安全账户：' + str(safe_account)
    
    charge_slider.reset()
    charge_image.setImage('charge_image.jpg')
    account_text.setText(safe_account_text)
    # reset charge_button to account for continued clicks & clear times on/off
    charge_button.reset()
    # keep track of which components have finished
    chargeComponents = [charge_slider, charge_image, account_text, charge_button]
    for thisComponent in chargeComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "charge" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # Run 'Each Frame' code from charge_code
        if charge_slider.getRating() is None :
            tmp_invest = 1
        else :
            tmp_invest = int(charge_slider.getRating())
        tmp_invest_text=str(tmp_invest)
        
        # *charge_slider* updates
        
        # if charge_slider is starting this frame...
        if charge_slider.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            charge_slider.frameNStart = frameN  # exact frame index
            charge_slider.tStart = t  # local t and not account for scr refresh
            charge_slider.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(charge_slider, 'tStartRefresh')  # time at next scr refresh
            # update status
            charge_slider.status = STARTED
            charge_slider.setAutoDraw(True)
        
        # if charge_slider is active this frame...
        if charge_slider.status == STARTED:
            # update params
            pass
        
        # *charge_image* updates
        
        # if charge_image is starting this frame...
        if charge_image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            charge_image.frameNStart = frameN  # exact frame index
            charge_image.tStart = t  # local t and not account for scr refresh
            charge_image.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(charge_image, 'tStartRefresh')  # time at next scr refresh
            # update status
            charge_image.status = STARTED
            charge_image.setAutoDraw(True)
        
        # if charge_image is active this frame...
        if charge_image.status == STARTED:
            # update params
            pass
        
        # *account_text* updates
        
        # if account_text is starting this frame...
        if account_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            account_text.frameNStart = frameN  # exact frame index
            account_text.tStart = t  # local t and not account for scr refresh
            account_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(account_text, 'tStartRefresh')  # time at next scr refresh
            # update status
            account_text.status = STARTED
            account_text.setAutoDraw(True)
        
        # if account_text is active this frame...
        if account_text.status == STARTED:
            # update params
            pass
        # *charge_button* updates
        
        # if charge_button is starting this frame...
        if charge_button.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            charge_button.frameNStart = frameN  # exact frame index
            charge_button.tStart = t  # local t and not account for scr refresh
            charge_button.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(charge_button, 'tStartRefresh')  # time at next scr refresh
            # update status
            charge_button.status = STARTED
            charge_button.setAutoDraw(True)
        
        # if charge_button is active this frame...
        if charge_button.status == STARTED:
            # update params
            charge_button.setText(tmp_invest_text, log=False)
            # check whether charge_button has been pressed
            if charge_button.isClicked:
                if not charge_button.wasClicked:
                    # if this is a new click, store time of first click and clicked until
                    charge_button.timesOn.append(charge_button.buttonClock.getTime())
                    charge_button.timesOff.append(charge_button.buttonClock.getTime())
                elif len(charge_button.timesOff):
                    # if click is continuing from last frame, update time of clicked until
                    charge_button.timesOff[-1] = charge_button.buttonClock.getTime()
                if not charge_button.wasClicked:
                    # end routine when charge_button is clicked
                    continueRoutine = False
                if not charge_button.wasClicked:
                    # run callback code when charge_button is clicked
                    pass
        # take note of whether charge_button was clicked, so that next frame we know if clicks are new
        charge_button.wasClicked = charge_button.isClicked and charge_button.status == STARTED
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
            if eyetracker:
                eyetracker.setConnectionState(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in chargeComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "charge" ---
    for thisComponent in chargeComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    prac_trials.addData('charge_slider.response', charge_slider.getRating())
    prac_trials.addData('charge_slider.rt', charge_slider.getRT())
    prac_trials.addData('charge_button.numClicks', charge_button.numClicks)
    if charge_button.numClicks:
       prac_trials.addData('charge_button.timesOn', charge_button.timesOn)
       prac_trials.addData('charge_button.timesOff', charge_button.timesOff)
    else:
       prac_trials.addData('charge_button.timesOn', "")
       prac_trials.addData('charge_button.timesOff', "")
    # the Routine "charge" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "trial" ---
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from trial_code
    balloonSize=initSize
    popped=False
    nPumps=0
    nVal = 0 # 有效充气
    inval_in = 0 # 无效充气次数
    noExpandList = [r1,r2,r3]
    event.clearEvents()
    
    invest_account_text = '投资账户：' + str(int(tmp_invest))
    pum_msg = '股市第0个交易日 \n 当前股价为' + str(int(tmp_invest))
    
    tri_num += 1
    
    tri_msg = '当前是第' + str(tri_num-3) + '轮，共30轮'
    Balloon.setImage('balloon.png')
    reminder_text.setText('按空格键充气\n按回车键中止')
    safeaccount_text.setText(safe_account_text)
    investaccount_text.setText(invest_account_text)
    bankButton_key_resp.keys = []
    bankButton_key_resp.rt = []
    _bankButton_key_resp_allKeys = []
    text.setText(tri_msg)
    # keep track of which components have finished
    trialComponents = [Balloon, reminder_text, safeaccount_text, investaccount_text, bankButton_key_resp, pumpwarning_text, text]
    for thisComponent in trialComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "trial" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # Run 'Each Frame' code from trial_code
        if event.getKeys(['space']):
            nPumps += 1
            nVal += 1
            if nPumps == lossPoint:
                popped=True
                continueRoutine=False
            elif nPumps in noExpandList:
                nVal -= 1
                inval_in += 1
        if event.getKeys(['return']):
            popped=False
            continueRoutine=False
        
        
        balloonSize=initSize + nVal * expandSize
        
        pum_msg = '股市第' + str(nPumps) + '个交易日 \n 当前股价为' + str(int(tmp_invest + nVal))
        
        
        # *Balloon* updates
        
        # if Balloon is starting this frame...
        if Balloon.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Balloon.frameNStart = frameN  # exact frame index
            Balloon.tStart = t  # local t and not account for scr refresh
            Balloon.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Balloon, 'tStartRefresh')  # time at next scr refresh
            # update status
            Balloon.status = STARTED
            Balloon.setAutoDraw(True)
        
        # if Balloon is active this frame...
        if Balloon.status == STARTED:
            # update params
            Balloon.setSize((balloonSize,balloonSize*2.2), log=False)
        
        # *reminder_text* updates
        
        # if reminder_text is starting this frame...
        if reminder_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            reminder_text.frameNStart = frameN  # exact frame index
            reminder_text.tStart = t  # local t and not account for scr refresh
            reminder_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(reminder_text, 'tStartRefresh')  # time at next scr refresh
            # update status
            reminder_text.status = STARTED
            reminder_text.setAutoDraw(True)
        
        # if reminder_text is active this frame...
        if reminder_text.status == STARTED:
            # update params
            pass
        
        # *safeaccount_text* updates
        
        # if safeaccount_text is starting this frame...
        if safeaccount_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            safeaccount_text.frameNStart = frameN  # exact frame index
            safeaccount_text.tStart = t  # local t and not account for scr refresh
            safeaccount_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(safeaccount_text, 'tStartRefresh')  # time at next scr refresh
            # update status
            safeaccount_text.status = STARTED
            safeaccount_text.setAutoDraw(True)
        
        # if safeaccount_text is active this frame...
        if safeaccount_text.status == STARTED:
            # update params
            pass
        
        # *investaccount_text* updates
        
        # if investaccount_text is starting this frame...
        if investaccount_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            investaccount_text.frameNStart = frameN  # exact frame index
            investaccount_text.tStart = t  # local t and not account for scr refresh
            investaccount_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(investaccount_text, 'tStartRefresh')  # time at next scr refresh
            # update status
            investaccount_text.status = STARTED
            investaccount_text.setAutoDraw(True)
        
        # if investaccount_text is active this frame...
        if investaccount_text.status == STARTED:
            # update params
            pass
        
        # *bankButton_key_resp* updates
        waitOnFlip = False
        
        # if bankButton_key_resp is starting this frame...
        if bankButton_key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            bankButton_key_resp.frameNStart = frameN  # exact frame index
            bankButton_key_resp.tStart = t  # local t and not account for scr refresh
            bankButton_key_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(bankButton_key_resp, 'tStartRefresh')  # time at next scr refresh
            # update status
            bankButton_key_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(bankButton_key_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(bankButton_key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if bankButton_key_resp.status == STARTED and not waitOnFlip:
            theseKeys = bankButton_key_resp.getKeys(keyList=['return'], waitRelease=False)
            _bankButton_key_resp_allKeys.extend(theseKeys)
            if len(_bankButton_key_resp_allKeys):
                bankButton_key_resp.keys = _bankButton_key_resp_allKeys[-1].name  # just the last key pressed
                bankButton_key_resp.rt = _bankButton_key_resp_allKeys[-1].rt
                bankButton_key_resp.duration = _bankButton_key_resp_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # *pumpwarning_text* updates
        
        # if pumpwarning_text is starting this frame...
        if pumpwarning_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            pumpwarning_text.frameNStart = frameN  # exact frame index
            pumpwarning_text.tStart = t  # local t and not account for scr refresh
            pumpwarning_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(pumpwarning_text, 'tStartRefresh')  # time at next scr refresh
            # update status
            pumpwarning_text.status = STARTED
            pumpwarning_text.setAutoDraw(True)
        
        # if pumpwarning_text is active this frame...
        if pumpwarning_text.status == STARTED:
            # update params
            pumpwarning_text.setText(pum_msg, log=False)
        
        # *text* updates
        
        # if text is starting this frame...
        if text.status == NOT_STARTED and tri_num>3:
            # keep track of start time/frame for later
            text.frameNStart = frameN  # exact frame index
            text.tStart = t  # local t and not account for scr refresh
            text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
            # update status
            text.status = STARTED
            text.setAutoDraw(True)
        
        # if text is active this frame...
        if text.status == STARTED:
            # update params
            pass
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
            if eyetracker:
                eyetracker.setConnectionState(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "trial" ---
    for thisComponent in trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # Run 'End Routine' code from trial_code
    if popped: 
        tmp_profit = (tmp_invest +  nPumps - inval_in) * (1 - probas) - tmp_invest
    else:
        if nPumps > 0:
            tmp_profit = (tmp_invest + nPumps - inval_in) * (1 + 0.002 * tmp_invest) - tmp_invest
        else :
            tmp_profit = 0
    tmp_profit = float("%.2f"%tmp_profit)
    safe_account += tmp_profit
    safe_account=float("%.2f"%safe_account)
    if period== 1 :
        thisExp.addData('nPumps', nPumps)
        thisExp.addData('size', balloonSize)
        thisExp.addData('inval_in', inval_in)
        thisExp.addData('safe_account', safe_account)
        thisExp.addData('invest', tmp_invest)
        thisExp.addData('popped', int(popped))
    
    # check responses
    if bankButton_key_resp.keys in ['', [], None]:  # No response was made
        bankButton_key_resp.keys = None
    prac_trials.addData('bankButton_key_resp.keys',bankButton_key_resp.keys)
    if bankButton_key_resp.keys != None:  # we had a response
        prac_trials.addData('bankButton_key_resp.rt', bankButton_key_resp.rt)
        prac_trials.addData('bankButton_key_resp.duration', bankButton_key_resp.duration)
    # the Routine "trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "feedback" ---
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from feedback_code
    #if popped :
    #    continueRoutine = True
    #else :
    #    continueRoutine = False
        
    event.clearEvents()
    stateSize = initSize
    stateImage = crackImageFile
    if popped==True:
        if int(probas) == 1:
            feedbackText='在第'+str(lossPoint) +'个交易日后，气球炸了！\n你的收益为:' + str(tmp_profit)+'\n请按回车键继续'
            bang.play()
        else:
            stateImage = imageFile
            feedbackText ='在第'+str(lossPoint) +'个交易日后，气球漏气了！\n你的收益为:'+ str(tmp_profit)+'\n请按回车键继续'
            leaky.play()
    else:
        feedbackText='气球将在第'+str(lossPoint) +'个交易日后爆炸/漏气，\n你的收益为:'+ str(tmp_profit)+'\n请按回车键继续'
        stateSize = balloonSize
        stateImage = imageFile
    feedback_image.setImage(stateImage)
    feedback_text.setText(feedbackText
)
    feedback_key_resp.keys = []
    feedback_key_resp.rt = []
    _feedback_key_resp_allKeys = []
    # keep track of which components have finished
    feedbackComponents = [feedback_image, feedback_text, feedback_key_resp]
    for thisComponent in feedbackComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "feedback" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *feedback_image* updates
        
        # if feedback_image is starting this frame...
        if feedback_image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            feedback_image.frameNStart = frameN  # exact frame index
            feedback_image.tStart = t  # local t and not account for scr refresh
            feedback_image.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(feedback_image, 'tStartRefresh')  # time at next scr refresh
            # update status
            feedback_image.status = STARTED
            feedback_image.setAutoDraw(True)
        
        # if feedback_image is active this frame...
        if feedback_image.status == STARTED:
            # update params
            pass
        
        # *feedback_text* updates
        
        # if feedback_text is starting this frame...
        if feedback_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            feedback_text.frameNStart = frameN  # exact frame index
            feedback_text.tStart = t  # local t and not account for scr refresh
            feedback_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(feedback_text, 'tStartRefresh')  # time at next scr refresh
            # update status
            feedback_text.status = STARTED
            feedback_text.setAutoDraw(True)
        
        # if feedback_text is active this frame...
        if feedback_text.status == STARTED:
            # update params
            pass
        
        # *feedback_key_resp* updates
        waitOnFlip = False
        
        # if feedback_key_resp is starting this frame...
        if feedback_key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            feedback_key_resp.frameNStart = frameN  # exact frame index
            feedback_key_resp.tStart = t  # local t and not account for scr refresh
            feedback_key_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(feedback_key_resp, 'tStartRefresh')  # time at next scr refresh
            # update status
            feedback_key_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(feedback_key_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(feedback_key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if feedback_key_resp.status == STARTED and not waitOnFlip:
            theseKeys = feedback_key_resp.getKeys(keyList=['return'], waitRelease=False)
            _feedback_key_resp_allKeys.extend(theseKeys)
            if len(_feedback_key_resp_allKeys):
                feedback_key_resp.keys = _feedback_key_resp_allKeys[-1].name  # just the last key pressed
                feedback_key_resp.rt = _feedback_key_resp_allKeys[-1].rt
                feedback_key_resp.duration = _feedback_key_resp_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
            if eyetracker:
                eyetracker.setConnectionState(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in feedbackComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "feedback" ---
    for thisComponent in feedbackComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if feedback_key_resp.keys in ['', [], None]:  # No response was made
        feedback_key_resp.keys = None
    prac_trials.addData('feedback_key_resp.keys',feedback_key_resp.keys)
    if feedback_key_resp.keys != None:  # we had a response
        prac_trials.addData('feedback_key_resp.rt', feedback_key_resp.rt)
        prac_trials.addData('feedback_key_resp.duration', feedback_key_resp.duration)
    # the Routine "feedback" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "assessment" ---
    continueRoutine = True
    # update component parameters for each repeat
    assessment_text.setText('本轮投资结束，看到收益结果后，\n如果感到后悔，请您评价自己的后悔程度\n（1表示稍微有点后悔，7表示非常后悔）')
    assessment_image.setImage('assessment_image.jpg')
    assessment_slider.reset()
    # keep track of which components have finished
    assessmentComponents = [assessment_text, assessment_image, assessment_slider]
    for thisComponent in assessmentComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "assessment" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *assessment_text* updates
        
        # if assessment_text is starting this frame...
        if assessment_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            assessment_text.frameNStart = frameN  # exact frame index
            assessment_text.tStart = t  # local t and not account for scr refresh
            assessment_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(assessment_text, 'tStartRefresh')  # time at next scr refresh
            # update status
            assessment_text.status = STARTED
            assessment_text.setAutoDraw(True)
        
        # if assessment_text is active this frame...
        if assessment_text.status == STARTED:
            # update params
            pass
        
        # *assessment_image* updates
        
        # if assessment_image is starting this frame...
        if assessment_image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            assessment_image.frameNStart = frameN  # exact frame index
            assessment_image.tStart = t  # local t and not account for scr refresh
            assessment_image.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(assessment_image, 'tStartRefresh')  # time at next scr refresh
            # update status
            assessment_image.status = STARTED
            assessment_image.setAutoDraw(True)
        
        # if assessment_image is active this frame...
        if assessment_image.status == STARTED:
            # update params
            pass
        
        # *assessment_slider* updates
        
        # if assessment_slider is starting this frame...
        if assessment_slider.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            assessment_slider.frameNStart = frameN  # exact frame index
            assessment_slider.tStart = t  # local t and not account for scr refresh
            assessment_slider.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(assessment_slider, 'tStartRefresh')  # time at next scr refresh
            # update status
            assessment_slider.status = STARTED
            assessment_slider.setAutoDraw(True)
        
        # if assessment_slider is active this frame...
        if assessment_slider.status == STARTED:
            # update params
            pass
        
        # Check assessment_slider for response to end routine
        if assessment_slider.getRating() is not None and assessment_slider.status == STARTED:
            continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
            if eyetracker:
                eyetracker.setConnectionState(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in assessmentComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "assessment" ---
    for thisComponent in assessmentComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    prac_trials.addData('assessment_slider.response', assessment_slider.getRating())
    prac_trials.addData('assessment_slider.rt', assessment_slider.getRT())
    # the Routine "assessment" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "earned" ---
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from earned_code
    event.clearEvents()
    tip_text = ''
    if period == 0:
        if prac_trials.thisTrialN == 2:
            continueRoutine=True
            tip_text ='您已经进行了%s次实验最终受益为：%.2f\n按空格键继续实验'%(\
                prac_trials.thisTrialN + 1, safe_account)
            prac_trials.finished = True
        else:
            continueRoutine=False
    else:
        if trials.thisTrialN == trials.nTotal - 1:
    #    if trials_exp.thisTrialN == 1:
            continueRoutine=True
            tip_text ='您已经进行了%s次实验最终受益为：%.2f\n按空格键继续实验'%(\
                trials.thisTrialN + 1, safe_account)
            trials.finished = True
        else:
            continueRoutine=False
    earned_text.setText(tip_text)
    earned_key_resp.keys = []
    earned_key_resp.rt = []
    _earned_key_resp_allKeys = []
    # keep track of which components have finished
    earnedComponents = [earned_text, earned_key_resp]
    for thisComponent in earnedComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "earned" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *earned_text* updates
        
        # if earned_text is starting this frame...
        if earned_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            earned_text.frameNStart = frameN  # exact frame index
            earned_text.tStart = t  # local t and not account for scr refresh
            earned_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(earned_text, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'earned_text.started')
            # update status
            earned_text.status = STARTED
            earned_text.setAutoDraw(True)
        
        # if earned_text is active this frame...
        if earned_text.status == STARTED:
            # update params
            pass
        
        # *earned_key_resp* updates
        waitOnFlip = False
        
        # if earned_key_resp is starting this frame...
        if earned_key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            earned_key_resp.frameNStart = frameN  # exact frame index
            earned_key_resp.tStart = t  # local t and not account for scr refresh
            earned_key_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(earned_key_resp, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'earned_key_resp.started')
            # update status
            earned_key_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(earned_key_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(earned_key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if earned_key_resp.status == STARTED and not waitOnFlip:
            theseKeys = earned_key_resp.getKeys(keyList=['space'], waitRelease=False)
            _earned_key_resp_allKeys.extend(theseKeys)
            if len(_earned_key_resp_allKeys):
                earned_key_resp.keys = _earned_key_resp_allKeys[-1].name  # just the last key pressed
                earned_key_resp.rt = _earned_key_resp_allKeys[-1].rt
                earned_key_resp.duration = _earned_key_resp_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
            if eyetracker:
                eyetracker.setConnectionState(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in earnedComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "earned" ---
    for thisComponent in earnedComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if earned_key_resp.keys in ['', [], None]:  # No response was made
        earned_key_resp.keys = None
    prac_trials.addData('earned_key_resp.keys',earned_key_resp.keys)
    if earned_key_resp.keys != None:  # we had a response
        prac_trials.addData('earned_key_resp.rt', earned_key_resp.rt)
        prac_trials.addData('earned_key_resp.duration', earned_key_resp.duration)
    # the Routine "earned" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'prac_trials'


# --- Prepare to start Routine "instructions" ---
continueRoutine = True
# update component parameters for each repeat
# Run 'Begin Routine' code from intro_code
safe_account =float('%.2f'%0.00)
instructions_key_resp.keys = []
instructions_key_resp.rt = []
_instructions_key_resp_allKeys = []
# keep track of which components have finished
instructionsComponents = [formal_image, instructions_key_resp]
for thisComponent in instructionsComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "instructions" ---
routineForceEnded = not continueRoutine
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *formal_image* updates
    
    # if formal_image is starting this frame...
    if formal_image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        formal_image.frameNStart = frameN  # exact frame index
        formal_image.tStart = t  # local t and not account for scr refresh
        formal_image.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(formal_image, 'tStartRefresh')  # time at next scr refresh
        # update status
        formal_image.status = STARTED
        formal_image.setAutoDraw(True)
    
    # if formal_image is active this frame...
    if formal_image.status == STARTED:
        # update params
        pass
    
    # *instructions_key_resp* updates
    waitOnFlip = False
    
    # if instructions_key_resp is starting this frame...
    if instructions_key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instructions_key_resp.frameNStart = frameN  # exact frame index
        instructions_key_resp.tStart = t  # local t and not account for scr refresh
        instructions_key_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructions_key_resp, 'tStartRefresh')  # time at next scr refresh
        # update status
        instructions_key_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(instructions_key_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(instructions_key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if instructions_key_resp.status == STARTED and not waitOnFlip:
        theseKeys = instructions_key_resp.getKeys(keyList=['space'], waitRelease=False)
        _instructions_key_resp_allKeys.extend(theseKeys)
        if len(_instructions_key_resp_allKeys):
            instructions_key_resp.keys = _instructions_key_resp_allKeys[-1].name  # just the last key pressed
            instructions_key_resp.rt = _instructions_key_resp_allKeys[-1].rt
            instructions_key_resp.duration = _instructions_key_resp_allKeys[-1].duration
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
        if eyetracker:
            eyetracker.setConnectionState(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "instructions" ---
for thisComponent in instructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if instructions_key_resp.keys in ['', [], None]:  # No response was made
    instructions_key_resp.keys = None
thisExp.addData('instructions_key_resp.keys',instructions_key_resp.keys)
if instructions_key_resp.keys != None:  # we had a response
    thisExp.addData('instructions_key_resp.rt', instructions_key_resp.rt)
    thisExp.addData('instructions_key_resp.duration', instructions_key_resp.duration)
thisExp.nextEntry()
# the Routine "instructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=1.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('exp_condi.xlsx'),
    seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial:
        exec('{} = thisTrial[paramName]'.format(paramName))

for thisTrial in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "charge" ---
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from charge_code
    tmp_invest =1
    safe_account_text = '安全账户：' + str(safe_account)
    
    charge_slider.reset()
    charge_image.setImage('charge_image.jpg')
    account_text.setText(safe_account_text)
    # reset charge_button to account for continued clicks & clear times on/off
    charge_button.reset()
    # keep track of which components have finished
    chargeComponents = [charge_slider, charge_image, account_text, charge_button]
    for thisComponent in chargeComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "charge" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # Run 'Each Frame' code from charge_code
        if charge_slider.getRating() is None :
            tmp_invest = 1
        else :
            tmp_invest = int(charge_slider.getRating())
        tmp_invest_text=str(tmp_invest)
        
        # *charge_slider* updates
        
        # if charge_slider is starting this frame...
        if charge_slider.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            charge_slider.frameNStart = frameN  # exact frame index
            charge_slider.tStart = t  # local t and not account for scr refresh
            charge_slider.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(charge_slider, 'tStartRefresh')  # time at next scr refresh
            # update status
            charge_slider.status = STARTED
            charge_slider.setAutoDraw(True)
        
        # if charge_slider is active this frame...
        if charge_slider.status == STARTED:
            # update params
            pass
        
        # *charge_image* updates
        
        # if charge_image is starting this frame...
        if charge_image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            charge_image.frameNStart = frameN  # exact frame index
            charge_image.tStart = t  # local t and not account for scr refresh
            charge_image.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(charge_image, 'tStartRefresh')  # time at next scr refresh
            # update status
            charge_image.status = STARTED
            charge_image.setAutoDraw(True)
        
        # if charge_image is active this frame...
        if charge_image.status == STARTED:
            # update params
            pass
        
        # *account_text* updates
        
        # if account_text is starting this frame...
        if account_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            account_text.frameNStart = frameN  # exact frame index
            account_text.tStart = t  # local t and not account for scr refresh
            account_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(account_text, 'tStartRefresh')  # time at next scr refresh
            # update status
            account_text.status = STARTED
            account_text.setAutoDraw(True)
        
        # if account_text is active this frame...
        if account_text.status == STARTED:
            # update params
            pass
        # *charge_button* updates
        
        # if charge_button is starting this frame...
        if charge_button.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            charge_button.frameNStart = frameN  # exact frame index
            charge_button.tStart = t  # local t and not account for scr refresh
            charge_button.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(charge_button, 'tStartRefresh')  # time at next scr refresh
            # update status
            charge_button.status = STARTED
            charge_button.setAutoDraw(True)
        
        # if charge_button is active this frame...
        if charge_button.status == STARTED:
            # update params
            charge_button.setText(tmp_invest_text, log=False)
            # check whether charge_button has been pressed
            if charge_button.isClicked:
                if not charge_button.wasClicked:
                    # if this is a new click, store time of first click and clicked until
                    charge_button.timesOn.append(charge_button.buttonClock.getTime())
                    charge_button.timesOff.append(charge_button.buttonClock.getTime())
                elif len(charge_button.timesOff):
                    # if click is continuing from last frame, update time of clicked until
                    charge_button.timesOff[-1] = charge_button.buttonClock.getTime()
                if not charge_button.wasClicked:
                    # end routine when charge_button is clicked
                    continueRoutine = False
                if not charge_button.wasClicked:
                    # run callback code when charge_button is clicked
                    pass
        # take note of whether charge_button was clicked, so that next frame we know if clicks are new
        charge_button.wasClicked = charge_button.isClicked and charge_button.status == STARTED
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
            if eyetracker:
                eyetracker.setConnectionState(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in chargeComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "charge" ---
    for thisComponent in chargeComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('charge_slider.response', charge_slider.getRating())
    trials.addData('charge_slider.rt', charge_slider.getRT())
    trials.addData('charge_button.numClicks', charge_button.numClicks)
    if charge_button.numClicks:
       trials.addData('charge_button.timesOn', charge_button.timesOn)
       trials.addData('charge_button.timesOff', charge_button.timesOff)
    else:
       trials.addData('charge_button.timesOn', "")
       trials.addData('charge_button.timesOff', "")
    # the Routine "charge" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "trial" ---
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from trial_code
    balloonSize=initSize
    popped=False
    nPumps=0
    nVal = 0 # 有效充气
    inval_in = 0 # 无效充气次数
    noExpandList = [r1,r2,r3]
    event.clearEvents()
    
    invest_account_text = '投资账户：' + str(int(tmp_invest))
    pum_msg = '股市第0个交易日 \n 当前股价为' + str(int(tmp_invest))
    
    tri_num += 1
    
    tri_msg = '当前是第' + str(tri_num-3) + '轮，共30轮'
    Balloon.setImage('balloon.png')
    reminder_text.setText('按空格键充气\n按回车键中止')
    safeaccount_text.setText(safe_account_text)
    investaccount_text.setText(invest_account_text)
    bankButton_key_resp.keys = []
    bankButton_key_resp.rt = []
    _bankButton_key_resp_allKeys = []
    text.setText(tri_msg)
    # keep track of which components have finished
    trialComponents = [Balloon, reminder_text, safeaccount_text, investaccount_text, bankButton_key_resp, pumpwarning_text, text]
    for thisComponent in trialComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "trial" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # Run 'Each Frame' code from trial_code
        if event.getKeys(['space']):
            nPumps += 1
            nVal += 1
            if nPumps == lossPoint:
                popped=True
                continueRoutine=False
            elif nPumps in noExpandList:
                nVal -= 1
                inval_in += 1
        if event.getKeys(['return']):
            popped=False
            continueRoutine=False
        
        
        balloonSize=initSize + nVal * expandSize
        
        pum_msg = '股市第' + str(nPumps) + '个交易日 \n 当前股价为' + str(int(tmp_invest + nVal))
        
        
        # *Balloon* updates
        
        # if Balloon is starting this frame...
        if Balloon.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Balloon.frameNStart = frameN  # exact frame index
            Balloon.tStart = t  # local t and not account for scr refresh
            Balloon.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Balloon, 'tStartRefresh')  # time at next scr refresh
            # update status
            Balloon.status = STARTED
            Balloon.setAutoDraw(True)
        
        # if Balloon is active this frame...
        if Balloon.status == STARTED:
            # update params
            Balloon.setSize((balloonSize,balloonSize*2.2), log=False)
        
        # *reminder_text* updates
        
        # if reminder_text is starting this frame...
        if reminder_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            reminder_text.frameNStart = frameN  # exact frame index
            reminder_text.tStart = t  # local t and not account for scr refresh
            reminder_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(reminder_text, 'tStartRefresh')  # time at next scr refresh
            # update status
            reminder_text.status = STARTED
            reminder_text.setAutoDraw(True)
        
        # if reminder_text is active this frame...
        if reminder_text.status == STARTED:
            # update params
            pass
        
        # *safeaccount_text* updates
        
        # if safeaccount_text is starting this frame...
        if safeaccount_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            safeaccount_text.frameNStart = frameN  # exact frame index
            safeaccount_text.tStart = t  # local t and not account for scr refresh
            safeaccount_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(safeaccount_text, 'tStartRefresh')  # time at next scr refresh
            # update status
            safeaccount_text.status = STARTED
            safeaccount_text.setAutoDraw(True)
        
        # if safeaccount_text is active this frame...
        if safeaccount_text.status == STARTED:
            # update params
            pass
        
        # *investaccount_text* updates
        
        # if investaccount_text is starting this frame...
        if investaccount_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            investaccount_text.frameNStart = frameN  # exact frame index
            investaccount_text.tStart = t  # local t and not account for scr refresh
            investaccount_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(investaccount_text, 'tStartRefresh')  # time at next scr refresh
            # update status
            investaccount_text.status = STARTED
            investaccount_text.setAutoDraw(True)
        
        # if investaccount_text is active this frame...
        if investaccount_text.status == STARTED:
            # update params
            pass
        
        # *bankButton_key_resp* updates
        waitOnFlip = False
        
        # if bankButton_key_resp is starting this frame...
        if bankButton_key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            bankButton_key_resp.frameNStart = frameN  # exact frame index
            bankButton_key_resp.tStart = t  # local t and not account for scr refresh
            bankButton_key_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(bankButton_key_resp, 'tStartRefresh')  # time at next scr refresh
            # update status
            bankButton_key_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(bankButton_key_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(bankButton_key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if bankButton_key_resp.status == STARTED and not waitOnFlip:
            theseKeys = bankButton_key_resp.getKeys(keyList=['return'], waitRelease=False)
            _bankButton_key_resp_allKeys.extend(theseKeys)
            if len(_bankButton_key_resp_allKeys):
                bankButton_key_resp.keys = _bankButton_key_resp_allKeys[-1].name  # just the last key pressed
                bankButton_key_resp.rt = _bankButton_key_resp_allKeys[-1].rt
                bankButton_key_resp.duration = _bankButton_key_resp_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # *pumpwarning_text* updates
        
        # if pumpwarning_text is starting this frame...
        if pumpwarning_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            pumpwarning_text.frameNStart = frameN  # exact frame index
            pumpwarning_text.tStart = t  # local t and not account for scr refresh
            pumpwarning_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(pumpwarning_text, 'tStartRefresh')  # time at next scr refresh
            # update status
            pumpwarning_text.status = STARTED
            pumpwarning_text.setAutoDraw(True)
        
        # if pumpwarning_text is active this frame...
        if pumpwarning_text.status == STARTED:
            # update params
            pumpwarning_text.setText(pum_msg, log=False)
        
        # *text* updates
        
        # if text is starting this frame...
        if text.status == NOT_STARTED and tri_num>3:
            # keep track of start time/frame for later
            text.frameNStart = frameN  # exact frame index
            text.tStart = t  # local t and not account for scr refresh
            text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
            # update status
            text.status = STARTED
            text.setAutoDraw(True)
        
        # if text is active this frame...
        if text.status == STARTED:
            # update params
            pass
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
            if eyetracker:
                eyetracker.setConnectionState(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "trial" ---
    for thisComponent in trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # Run 'End Routine' code from trial_code
    if popped: 
        tmp_profit = (tmp_invest +  nPumps - inval_in) * (1 - probas) - tmp_invest
    else:
        if nPumps > 0:
            tmp_profit = (tmp_invest + nPumps - inval_in) * (1 + 0.002 * tmp_invest) - tmp_invest
        else :
            tmp_profit = 0
    tmp_profit = float("%.2f"%tmp_profit)
    safe_account += tmp_profit
    safe_account=float("%.2f"%safe_account)
    if period== 1 :
        thisExp.addData('nPumps', nPumps)
        thisExp.addData('size', balloonSize)
        thisExp.addData('inval_in', inval_in)
        thisExp.addData('safe_account', safe_account)
        thisExp.addData('invest', tmp_invest)
        thisExp.addData('popped', int(popped))
    
    # check responses
    if bankButton_key_resp.keys in ['', [], None]:  # No response was made
        bankButton_key_resp.keys = None
    trials.addData('bankButton_key_resp.keys',bankButton_key_resp.keys)
    if bankButton_key_resp.keys != None:  # we had a response
        trials.addData('bankButton_key_resp.rt', bankButton_key_resp.rt)
        trials.addData('bankButton_key_resp.duration', bankButton_key_resp.duration)
    # the Routine "trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "feedback" ---
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from feedback_code
    #if popped :
    #    continueRoutine = True
    #else :
    #    continueRoutine = False
        
    event.clearEvents()
    stateSize = initSize
    stateImage = crackImageFile
    if popped==True:
        if int(probas) == 1:
            feedbackText='在第'+str(lossPoint) +'个交易日后，气球炸了！\n你的收益为:' + str(tmp_profit)+'\n请按回车键继续'
            bang.play()
        else:
            stateImage = imageFile
            feedbackText ='在第'+str(lossPoint) +'个交易日后，气球漏气了！\n你的收益为:'+ str(tmp_profit)+'\n请按回车键继续'
            leaky.play()
    else:
        feedbackText='气球将在第'+str(lossPoint) +'个交易日后爆炸/漏气，\n你的收益为:'+ str(tmp_profit)+'\n请按回车键继续'
        stateSize = balloonSize
        stateImage = imageFile
    feedback_image.setImage(stateImage)
    feedback_text.setText(feedbackText
)
    feedback_key_resp.keys = []
    feedback_key_resp.rt = []
    _feedback_key_resp_allKeys = []
    # keep track of which components have finished
    feedbackComponents = [feedback_image, feedback_text, feedback_key_resp]
    for thisComponent in feedbackComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "feedback" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *feedback_image* updates
        
        # if feedback_image is starting this frame...
        if feedback_image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            feedback_image.frameNStart = frameN  # exact frame index
            feedback_image.tStart = t  # local t and not account for scr refresh
            feedback_image.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(feedback_image, 'tStartRefresh')  # time at next scr refresh
            # update status
            feedback_image.status = STARTED
            feedback_image.setAutoDraw(True)
        
        # if feedback_image is active this frame...
        if feedback_image.status == STARTED:
            # update params
            pass
        
        # *feedback_text* updates
        
        # if feedback_text is starting this frame...
        if feedback_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            feedback_text.frameNStart = frameN  # exact frame index
            feedback_text.tStart = t  # local t and not account for scr refresh
            feedback_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(feedback_text, 'tStartRefresh')  # time at next scr refresh
            # update status
            feedback_text.status = STARTED
            feedback_text.setAutoDraw(True)
        
        # if feedback_text is active this frame...
        if feedback_text.status == STARTED:
            # update params
            pass
        
        # *feedback_key_resp* updates
        waitOnFlip = False
        
        # if feedback_key_resp is starting this frame...
        if feedback_key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            feedback_key_resp.frameNStart = frameN  # exact frame index
            feedback_key_resp.tStart = t  # local t and not account for scr refresh
            feedback_key_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(feedback_key_resp, 'tStartRefresh')  # time at next scr refresh
            # update status
            feedback_key_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(feedback_key_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(feedback_key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if feedback_key_resp.status == STARTED and not waitOnFlip:
            theseKeys = feedback_key_resp.getKeys(keyList=['return'], waitRelease=False)
            _feedback_key_resp_allKeys.extend(theseKeys)
            if len(_feedback_key_resp_allKeys):
                feedback_key_resp.keys = _feedback_key_resp_allKeys[-1].name  # just the last key pressed
                feedback_key_resp.rt = _feedback_key_resp_allKeys[-1].rt
                feedback_key_resp.duration = _feedback_key_resp_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
            if eyetracker:
                eyetracker.setConnectionState(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in feedbackComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "feedback" ---
    for thisComponent in feedbackComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if feedback_key_resp.keys in ['', [], None]:  # No response was made
        feedback_key_resp.keys = None
    trials.addData('feedback_key_resp.keys',feedback_key_resp.keys)
    if feedback_key_resp.keys != None:  # we had a response
        trials.addData('feedback_key_resp.rt', feedback_key_resp.rt)
        trials.addData('feedback_key_resp.duration', feedback_key_resp.duration)
    # the Routine "feedback" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "assessment" ---
    continueRoutine = True
    # update component parameters for each repeat
    assessment_text.setText('本轮投资结束，看到收益结果后，\n如果感到后悔，请您评价自己的后悔程度\n（1表示稍微有点后悔，7表示非常后悔）')
    assessment_image.setImage('assessment_image.jpg')
    assessment_slider.reset()
    # keep track of which components have finished
    assessmentComponents = [assessment_text, assessment_image, assessment_slider]
    for thisComponent in assessmentComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "assessment" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *assessment_text* updates
        
        # if assessment_text is starting this frame...
        if assessment_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            assessment_text.frameNStart = frameN  # exact frame index
            assessment_text.tStart = t  # local t and not account for scr refresh
            assessment_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(assessment_text, 'tStartRefresh')  # time at next scr refresh
            # update status
            assessment_text.status = STARTED
            assessment_text.setAutoDraw(True)
        
        # if assessment_text is active this frame...
        if assessment_text.status == STARTED:
            # update params
            pass
        
        # *assessment_image* updates
        
        # if assessment_image is starting this frame...
        if assessment_image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            assessment_image.frameNStart = frameN  # exact frame index
            assessment_image.tStart = t  # local t and not account for scr refresh
            assessment_image.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(assessment_image, 'tStartRefresh')  # time at next scr refresh
            # update status
            assessment_image.status = STARTED
            assessment_image.setAutoDraw(True)
        
        # if assessment_image is active this frame...
        if assessment_image.status == STARTED:
            # update params
            pass
        
        # *assessment_slider* updates
        
        # if assessment_slider is starting this frame...
        if assessment_slider.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            assessment_slider.frameNStart = frameN  # exact frame index
            assessment_slider.tStart = t  # local t and not account for scr refresh
            assessment_slider.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(assessment_slider, 'tStartRefresh')  # time at next scr refresh
            # update status
            assessment_slider.status = STARTED
            assessment_slider.setAutoDraw(True)
        
        # if assessment_slider is active this frame...
        if assessment_slider.status == STARTED:
            # update params
            pass
        
        # Check assessment_slider for response to end routine
        if assessment_slider.getRating() is not None and assessment_slider.status == STARTED:
            continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
            if eyetracker:
                eyetracker.setConnectionState(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in assessmentComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "assessment" ---
    for thisComponent in assessmentComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('assessment_slider.response', assessment_slider.getRating())
    trials.addData('assessment_slider.rt', assessment_slider.getRT())
    # the Routine "assessment" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "earned" ---
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from earned_code
    event.clearEvents()
    tip_text = ''
    if period == 0:
        if prac_trials.thisTrialN == 2:
            continueRoutine=True
            tip_text ='您已经进行了%s次实验最终受益为：%.2f\n按空格键继续实验'%(\
                prac_trials.thisTrialN + 1, safe_account)
            prac_trials.finished = True
        else:
            continueRoutine=False
    else:
        if trials.thisTrialN == trials.nTotal - 1:
    #    if trials_exp.thisTrialN == 1:
            continueRoutine=True
            tip_text ='您已经进行了%s次实验最终受益为：%.2f\n按空格键继续实验'%(\
                trials.thisTrialN + 1, safe_account)
            trials.finished = True
        else:
            continueRoutine=False
    earned_text.setText(tip_text)
    earned_key_resp.keys = []
    earned_key_resp.rt = []
    _earned_key_resp_allKeys = []
    # keep track of which components have finished
    earnedComponents = [earned_text, earned_key_resp]
    for thisComponent in earnedComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "earned" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *earned_text* updates
        
        # if earned_text is starting this frame...
        if earned_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            earned_text.frameNStart = frameN  # exact frame index
            earned_text.tStart = t  # local t and not account for scr refresh
            earned_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(earned_text, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'earned_text.started')
            # update status
            earned_text.status = STARTED
            earned_text.setAutoDraw(True)
        
        # if earned_text is active this frame...
        if earned_text.status == STARTED:
            # update params
            pass
        
        # *earned_key_resp* updates
        waitOnFlip = False
        
        # if earned_key_resp is starting this frame...
        if earned_key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            earned_key_resp.frameNStart = frameN  # exact frame index
            earned_key_resp.tStart = t  # local t and not account for scr refresh
            earned_key_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(earned_key_resp, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'earned_key_resp.started')
            # update status
            earned_key_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(earned_key_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(earned_key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if earned_key_resp.status == STARTED and not waitOnFlip:
            theseKeys = earned_key_resp.getKeys(keyList=['space'], waitRelease=False)
            _earned_key_resp_allKeys.extend(theseKeys)
            if len(_earned_key_resp_allKeys):
                earned_key_resp.keys = _earned_key_resp_allKeys[-1].name  # just the last key pressed
                earned_key_resp.rt = _earned_key_resp_allKeys[-1].rt
                earned_key_resp.duration = _earned_key_resp_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
            if eyetracker:
                eyetracker.setConnectionState(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in earnedComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "earned" ---
    for thisComponent in earnedComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if earned_key_resp.keys in ['', [], None]:  # No response was made
        earned_key_resp.keys = None
    trials.addData('earned_key_resp.keys',earned_key_resp.keys)
    if earned_key_resp.keys != None:  # we had a response
        trials.addData('earned_key_resp.rt', earned_key_resp.rt)
        trials.addData('earned_key_resp.duration', earned_key_resp.duration)
    # the Routine "earned" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'trials'


# --- Prepare to start Routine "ending" ---
continueRoutine = True
# update component parameters for each repeat
ending_key_resp.keys = []
ending_key_resp.rt = []
_ending_key_resp_allKeys = []
# keep track of which components have finished
endingComponents = [ending_text, ending_key_resp]
for thisComponent in endingComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "ending" ---
routineForceEnded = not continueRoutine
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *ending_text* updates
    
    # if ending_text is starting this frame...
    if ending_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        ending_text.frameNStart = frameN  # exact frame index
        ending_text.tStart = t  # local t and not account for scr refresh
        ending_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(ending_text, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'ending_text.started')
        # update status
        ending_text.status = STARTED
        ending_text.setAutoDraw(True)
    
    # if ending_text is active this frame...
    if ending_text.status == STARTED:
        # update params
        pass
    
    # *ending_key_resp* updates
    waitOnFlip = False
    
    # if ending_key_resp is starting this frame...
    if ending_key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        ending_key_resp.frameNStart = frameN  # exact frame index
        ending_key_resp.tStart = t  # local t and not account for scr refresh
        ending_key_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(ending_key_resp, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'ending_key_resp.started')
        # update status
        ending_key_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(ending_key_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(ending_key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if ending_key_resp.status == STARTED and not waitOnFlip:
        theseKeys = ending_key_resp.getKeys(keyList=['space'], waitRelease=False)
        _ending_key_resp_allKeys.extend(theseKeys)
        if len(_ending_key_resp_allKeys):
            ending_key_resp.keys = _ending_key_resp_allKeys[-1].name  # just the last key pressed
            ending_key_resp.rt = _ending_key_resp_allKeys[-1].rt
            ending_key_resp.duration = _ending_key_resp_allKeys[-1].duration
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
        if eyetracker:
            eyetracker.setConnectionState(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in endingComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "ending" ---
for thisComponent in endingComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if ending_key_resp.keys in ['', [], None]:  # No response was made
    ending_key_resp.keys = None
thisExp.addData('ending_key_resp.keys',ending_key_resp.keys)
if ending_key_resp.keys != None:  # we had a response
    thisExp.addData('ending_key_resp.rt', ending_key_resp.rt)
    thisExp.addData('ending_key_resp.duration', ending_key_resp.duration)
thisExp.nextEntry()
# the Routine "ending" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- End experiment ---
# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
if eyetracker:
    eyetracker.setConnectionState(False)
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
