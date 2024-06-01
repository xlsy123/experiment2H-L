/******************** 
 * Experiment2 Test *
 ********************/

import { core, data, sound, util, visual, hardware } from './lib/psychojs-2023.1.3.js';
const { PsychoJS } = core;
const { TrialHandler, MultiStairHandler } = data;
const { Scheduler } = util;
//some handy aliases as in the psychopy scripts;
const { abs, sin, cos, PI: pi, sqrt } = Math;
const { round } = util;


// store info about the experiment session:
let expName = 'experiment2';  // from the Builder filename that created this script
let expInfo = {
    'participant': '',
    'age': '',
    'gender': ["\u7537", "\u5973"],
};

// Start code blocks for 'Before Experiment'
// init psychoJS:
const psychoJS = new PsychoJS({
  debug: true
});

// open window:
psychoJS.openWindow({
  fullscr: true,
  color: new util.Color([0,0,0]),
  units: 'height',
  waitBlanking: true
});
// schedule the experiment:
psychoJS.schedule(psychoJS.gui.DlgFromDict({
  dictionary: expInfo,
  title: expName
}));

const flowScheduler = new Scheduler(psychoJS);
const dialogCancelScheduler = new Scheduler(psychoJS);
psychoJS.scheduleCondition(function() { return (psychoJS.gui.dialogComponent.button === 'OK'); }, flowScheduler, dialogCancelScheduler);

// flowScheduler gets run if the participants presses OK
flowScheduler.add(updateInfo); // add timeStamp
flowScheduler.add(experimentInit);
flowScheduler.add(introRoutineBegin());
flowScheduler.add(introRoutineEachFrame());
flowScheduler.add(introRoutineEnd());
flowScheduler.add(intro_2RoutineBegin());
flowScheduler.add(intro_2RoutineEachFrame());
flowScheduler.add(intro_2RoutineEnd());
flowScheduler.add(instruction_pracRoutineBegin());
flowScheduler.add(instruction_pracRoutineEachFrame());
flowScheduler.add(instruction_pracRoutineEnd());
const prac_trialsLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(prac_trialsLoopBegin(prac_trialsLoopScheduler));
flowScheduler.add(prac_trialsLoopScheduler);
flowScheduler.add(prac_trialsLoopEnd);
flowScheduler.add(introRoutineBegin());
flowScheduler.add(introRoutineEachFrame());
flowScheduler.add(introRoutineEnd());
flowScheduler.add(formal_intro2RoutineBegin());
flowScheduler.add(formal_intro2RoutineEachFrame());
flowScheduler.add(formal_intro2RoutineEnd());
flowScheduler.add(instructionsRoutineBegin());
flowScheduler.add(instructionsRoutineEachFrame());
flowScheduler.add(instructionsRoutineEnd());
const trialsLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(trialsLoopBegin(trialsLoopScheduler));
flowScheduler.add(trialsLoopScheduler);
flowScheduler.add(trialsLoopEnd);
flowScheduler.add(relaxRoutineBegin());
flowScheduler.add(relaxRoutineEachFrame());
flowScheduler.add(relaxRoutineEnd());
flowScheduler.add(introRoutineBegin());
flowScheduler.add(introRoutineEachFrame());
flowScheduler.add(introRoutineEnd());
const trials_2LoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(trials_2LoopBegin(trials_2LoopScheduler));
flowScheduler.add(trials_2LoopScheduler);
flowScheduler.add(trials_2LoopEnd);
flowScheduler.add(endingRoutineBegin());
flowScheduler.add(endingRoutineEachFrame());
flowScheduler.add(endingRoutineEnd());
flowScheduler.add(quitPsychoJS, '', true);

// quit if user presses Cancel in dialog box:
dialogCancelScheduler.add(quitPsychoJS, '', false);

psychoJS.start({
  expName: expName,
  expInfo: expInfo,
  resources: [
    // resources:
    {'name': 'exp_condi_pra.xlsx', 'path': 'exp_condi_pra.xlsx'},
    {'name': 'balloon.png', 'path': 'balloon.png'},
    {'name': 'balloon_crack.png', 'path': 'balloon_crack.png'},
    {'name': 'exp_condi_H.xlsx', 'path': 'exp_condi_H.xlsx'},
    {'name': 'balloon.png', 'path': 'balloon.png'},
    {'name': 'balloon_crack.png', 'path': 'balloon_crack.png'},
    {'name': 'exp_condi_L.xlsx', 'path': 'exp_condi_L.xlsx'},
    {'name': 'balloon.png', 'path': 'balloon.png'},
    {'name': 'balloon_crack.png', 'path': 'balloon_crack.png'},
    {'name': 'intro_image.jpg', 'path': 'intro_image.jpg'},
    {'name': 'intro_image2.jpg', 'path': 'intro_image2.jpg'},
    {'name': 'intro_prac_image.jpg', 'path': 'intro_prac_image.jpg'},
    {'name': 'charge_image.jpg', 'path': 'charge_image.jpg'},
    {'name': 'default.png', 'path': 'https://pavlovia.org/assets/default/default.png'},
    {'name': 'balloon.png', 'path': 'balloon.png'},
    {'name': 'assessment_image.jpg', 'path': 'assessment_image.jpg'},
    {'name': 'formal_intro_image.jpg', 'path': 'formal_intro_image.jpg'},
    {'name': 'formal_image.jpg', 'path': 'formal_image.jpg'},
    {'name': 'relax.jpg', 'path': 'relax.jpg'},
    {'name': 'clock.mp4', 'path': 'clock.mp4'},
    {'name': 'thanks.jpg', 'path': 'thanks.jpg'},
  ]
});

psychoJS.experimentLogger.setLevel(core.Logger.ServerLevel.EXP);

async function updateInfo() {
  currentLoop = psychoJS.experiment;  // right now there are no loops
  expInfo['date'] = util.MonotonicClock.getDateStr();  // add a simple timestamp
  expInfo['expName'] = expName;
  expInfo['psychopyVersion'] = '2023.1.3';
  expInfo['OS'] = window.navigator.platform;


  // store frame rate of monitor if we can measure it successfully
  expInfo['frameRate'] = psychoJS.window.getActualFrameRate();
  if (typeof expInfo['frameRate'] !== 'undefined')
    frameDur = 1.0 / Math.round(expInfo['frameRate']);
  else
    frameDur = 1.0 / 60.0; // couldn't get a reliable measure so guess

  // add info from the URL:
  util.addInfoFromUrl(expInfo);
  

  
  psychoJS.experiment.dataFileName = (("." + "/") + `data/${expInfo["participant"]}_${expName}_${expInfo["date"]}`);


  return Scheduler.Event.NEXT;
}

async function experimentInit() {
  // Initialize components for Routine "intro"
  introClock = new util.Clock();
  intro_image = new visual.ImageStim({
    win : psychoJS.window,
    name : 'intro_image', units : undefined, 
    image : 'intro_image.jpg', mask : undefined,
    anchor : 'center',
    ori : 0.0, pos : [0, 0], size : [1.1, 0.8],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 512.0, interpolate : true, depth : 0.0 
  });
  intro_key_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "intro_2"
  intro_2Clock = new util.Clock();
  intro_image2 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'intro_image2', units : undefined, 
    image : 'intro_image2.jpg', mask : undefined,
    anchor : 'center',
    ori : 0.0, pos : [0, 0], size : [1.1, 0.8],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : 0.0 
  });
  intro_2key_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "instruction_prac"
  instruction_pracClock = new util.Clock();
  instruction_prac_image = new visual.ImageStim({
    win : psychoJS.window,
    name : 'instruction_prac_image', units : undefined, 
    image : 'intro_prac_image.jpg', mask : undefined,
    anchor : 'center',
    ori : 0.0, pos : [0, 0], size : [1.1, 0.8],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : 0.0 
  });
  instruction_prac_key_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Run 'Begin Experiment' code from instruction_prac_code
  safe_account = Number.parseFloat(`${0}`);
  
  // Initialize components for Routine "charge"
  chargeClock = new util.Clock();
  charge_slider = new visual.Slider({
    win: psychoJS.window, name: 'charge_slider',
    startValue: 1,
    size: [1.0, 0.1], pos: [0, (- 0.2)], ori: 0.0, units: psychoJS.window.units,
    labels: [1, 100], fontSize: 0.05, ticks: [1, 100],
    granularity: 1.0, style: ["RATING", "TRIANGLE_MARKER"],
    color: new util.Color('LightGray'), markerColor: new util.Color('blue'), lineColor: new util.Color('black'), 
    opacity: undefined, fontFamily: 'Open Sans', bold: true, italic: false, depth: -1, 
    flip: false,
  });
  
  charge_image = new visual.ImageStim({
    win : psychoJS.window,
    name : 'charge_image', units : undefined, 
    image : 'default.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, pos : [0, 0.1], size : [0.96, 0.4],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -2.0 
  });
  account_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'account_text',
    text: '',
    font: 'Open Sans',
    units: undefined, 
    pos: [(- 0.45), 0.37], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: -3.0 
  });
  
  charge_button = new visual.ButtonStim({
    win: psychoJS.window,
    name: 'charge_button',
    text: '',
    fillColor: [0.9216, 0.9216, 0.7255],
    borderColor: null,
    color: 'black',
    colorSpace: 'rgb',
    pos: [0, (- 0.35)],
    letterHeight: 0.05,
    size: [0.3, 0.1],
    depth: -4
  });
  charge_button.clock = new util.Clock();
  
  // Initialize components for Routine "trial"
  trialClock = new util.Clock();
  // Run 'Begin Experiment' code from trial_code
  initSize = 0.1;
  expandSize = 0.0015;
  balloonSize = 0.1;
  
  Balloon = new visual.ImageStim({
    win : psychoJS.window,
    name : 'Balloon', units : 'norm', 
    image : 'default.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, pos : [0, 0], size : 1.0,
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -1.0 
  });
  reminder_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'reminder_text',
    text: '',
    font: 'Times New Roman',
    units: 'height', 
    pos: [0, 0.37], height: 0.04,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: -2.0 
  });
  
  safeaccount_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'safeaccount_text',
    text: '',
    font: 'Open Sans',
    units: undefined, 
    pos: [(- 0.45), 0.37], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: -3.0 
  });
  
  investaccount_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'investaccount_text',
    text: '',
    font: 'Open Sans',
    units: undefined, 
    pos: [0.45, 0.37], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: -4.0 
  });
  
  bankButton_key_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  pumpwarning_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'pumpwarning_text',
    text: '',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, (- 0.3)], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: -6.0 
  });
  
  text = new visual.TextStim({
    win: psychoJS.window,
    name: 'text',
    text: '',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0.3], height: 0.03,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: -7.0 
  });
  
  // Initialize components for Routine "feedback"
  feedbackClock = new util.Clock();
  // Run 'Begin Experiment' code from feedback_code
  import {sound} from 'psychopy';
  feedbackText = "";
  bang = new sound.Sound("bang.wav");
  leaky = new sound.Sound("leaky.wav");
  
  feedback_image = new visual.ImageStim({
    win : psychoJS.window,
    name : 'feedback_image', units : undefined, 
    image : 'default.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, pos : [0, 0.1], size : [0.15, 0.22],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -1.0 
  });
  feedback_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'feedback_text',
    text: '',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, (- 0.2)], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: -2.0 
  });
  
  feedback_key_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "assessment"
  assessmentClock = new util.Clock();
  assessment_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'assessment_text',
    text: '',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0.1], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: 0.0 
  });
  
  assessment_image = new visual.ImageStim({
    win : psychoJS.window,
    name : 'assessment_image', units : undefined, 
    image : 'default.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, pos : [0, 0.05], size : [1, 0.4],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -1.0 
  });
  assessment_slider = new visual.Slider({
    win: psychoJS.window, name: 'assessment_slider',
    startValue: undefined,
    size: [1.0, 0.1], pos: [0, (- 0.2)], ori: 0.0, units: psychoJS.window.units,
    labels: [1, 2, 3, 4, 5, 6, 7], fontSize: 0.05, ticks: [1, 2, 3, 4, 5, 6, 7],
    granularity: 1.0, style: ["RATING", "LABELS_45"],
    color: new util.Color('black'), markerColor: new util.Color('black'), lineColor: new util.Color('black'), 
    opacity: undefined, fontFamily: 'Open Sans', bold: true, italic: false, depth: -2, 
    flip: false,
  });
  
  // Initialize components for Routine "earned"
  earnedClock = new util.Clock();
  earned_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'earned_text',
    text: '',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: -1.0 
  });
  
  earned_key_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "formal_intro2"
  formal_intro2Clock = new util.Clock();
  formal_intro_image = new visual.ImageStim({
    win : psychoJS.window,
    name : 'formal_intro_image', units : undefined, 
    image : 'formal_intro_image.jpg', mask : undefined,
    anchor : 'center',
    ori : 0.0, pos : [0, 0], size : [1.1, 0.8],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : 0.0 
  });
  formal_intro_key_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "instructions"
  instructionsClock = new util.Clock();
  formal_image = new visual.ImageStim({
    win : psychoJS.window,
    name : 'formal_image', units : undefined, 
    image : 'formal_image.jpg', mask : undefined,
    anchor : 'center',
    ori : 0.0, pos : [0, 0], size : [1.1, 0.85],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -1.0 
  });
  instructions_key_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "relax"
  relaxClock = new util.Clock();
  relax_key_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  relax_image = new visual.ImageStim({
    win : psychoJS.window,
    name : 'relax_image', units : undefined, 
    image : 'relax.jpg', mask : undefined,
    anchor : 'center',
    ori : 0.0, pos : [0, 0], size : [1.1, 0.8],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -2.0 
  });
  clock_movieClock = new util.Clock();
  clock_movie = new visual.MovieStim({
    win: psychoJS.window,
    name: 'clock_movie',
    units: psychoJS.window.units,
    movie: 'clock.mp4',
    pos: [0, (- 0.35)],
    anchor: 'center',
    size: [0.3, 0.18],
    ori: 0.0,
    opacity: undefined,
    loop: false,
    noAudio: false,
    depth: -3
    });
  // Initialize components for Routine "ending"
  endingClock = new util.Clock();
  ending_image = new visual.ImageStim({
    win : psychoJS.window,
    name : 'ending_image', units : undefined, 
    image : 'thanks.jpg', mask : undefined,
    anchor : 'center',
    ori : 0.0, pos : [0, 0], size : [1.1, 0.8],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : 0.0 
  });
  ending_key_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Create some handy timers
  globalClock = new util.Clock();  // to track the time since experiment started
  routineTimer = new util.CountdownTimer();  // to track time remaining of each (non-slip) routine
  
  return Scheduler.Event.NEXT;
}

function introRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'intro' ---
    t = 0;
    introClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    intro_key_resp.keys = undefined;
    intro_key_resp.rt = undefined;
    _intro_key_resp_allKeys = [];
    // keep track of which components have finished
    introComponents = [];
    introComponents.push(intro_image);
    introComponents.push(intro_key_resp);
    
    for (const thisComponent of introComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}

function introRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'intro' ---
    // get current time
    t = introClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *intro_image* updates
    if (t >= 0.0 && intro_image.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      intro_image.tStart = t;  // (not accounting for frame time here)
      intro_image.frameNStart = frameN;  // exact frame index
      
      intro_image.setAutoDraw(true);
    }

    
    // *intro_key_resp* updates
    if (t >= 0.0 && intro_key_resp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      intro_key_resp.tStart = t;  // (not accounting for frame time here)
      intro_key_resp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { intro_key_resp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { intro_key_resp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { intro_key_resp.clearEvents(); });
    }

    if (intro_key_resp.status === PsychoJS.Status.STARTED) {
      let theseKeys = intro_key_resp.getKeys({keyList: ['space'], waitRelease: false});
      _intro_key_resp_allKeys = _intro_key_resp_allKeys.concat(theseKeys);
      if (_intro_key_resp_allKeys.length > 0) {
        intro_key_resp.keys = _intro_key_resp_allKeys[_intro_key_resp_allKeys.length - 1].name;  // just the last key pressed
        intro_key_resp.rt = _intro_key_resp_allKeys[_intro_key_resp_allKeys.length - 1].rt;
        intro_key_resp.duration = _intro_key_resp_allKeys[_intro_key_resp_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of introComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}

function introRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'intro' ---
    for (const thisComponent of introComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(intro_key_resp.corr, level);
    }
    psychoJS.experiment.addData('intro_key_resp.keys', intro_key_resp.keys);
    if (typeof intro_key_resp.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('intro_key_resp.rt', intro_key_resp.rt);
        psychoJS.experiment.addData('intro_key_resp.duration', intro_key_resp.duration);
        routineTimer.reset();
        }
    
    intro_key_resp.stop();
    // the Routine "intro" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}

function intro_2RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'intro_2' ---
    t = 0;
    intro_2Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    intro_2key_resp.keys = undefined;
    intro_2key_resp.rt = undefined;
    _intro_2key_resp_allKeys = [];
    // keep track of which components have finished
    intro_2Components = [];
    intro_2Components.push(intro_image2);
    intro_2Components.push(intro_2key_resp);
    
    for (const thisComponent of intro_2Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}

function intro_2RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'intro_2' ---
    // get current time
    t = intro_2Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *intro_image2* updates
    if (t >= 0.0 && intro_image2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      intro_image2.tStart = t;  // (not accounting for frame time here)
      intro_image2.frameNStart = frameN;  // exact frame index
      
      intro_image2.setAutoDraw(true);
    }

    
    // *intro_2key_resp* updates
    if (t >= 0.0 && intro_2key_resp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      intro_2key_resp.tStart = t;  // (not accounting for frame time here)
      intro_2key_resp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { intro_2key_resp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { intro_2key_resp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { intro_2key_resp.clearEvents(); });
    }

    if (intro_2key_resp.status === PsychoJS.Status.STARTED) {
      let theseKeys = intro_2key_resp.getKeys({keyList: ['space'], waitRelease: false});
      _intro_2key_resp_allKeys = _intro_2key_resp_allKeys.concat(theseKeys);
      if (_intro_2key_resp_allKeys.length > 0) {
        intro_2key_resp.keys = _intro_2key_resp_allKeys[_intro_2key_resp_allKeys.length - 1].name;  // just the last key pressed
        intro_2key_resp.rt = _intro_2key_resp_allKeys[_intro_2key_resp_allKeys.length - 1].rt;
        intro_2key_resp.duration = _intro_2key_resp_allKeys[_intro_2key_resp_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of intro_2Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}

function intro_2RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'intro_2' ---
    for (const thisComponent of intro_2Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(intro_2key_resp.corr, level);
    }
    psychoJS.experiment.addData('intro_2key_resp.keys', intro_2key_resp.keys);
    if (typeof intro_2key_resp.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('intro_2key_resp.rt', intro_2key_resp.rt);
        psychoJS.experiment.addData('intro_2key_resp.duration', intro_2key_resp.duration);
        routineTimer.reset();
        }
    
    intro_2key_resp.stop();
    // the Routine "intro_2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}

function instruction_pracRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'instruction_prac' ---
    t = 0;
    instruction_pracClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    instruction_prac_key_resp.keys = undefined;
    instruction_prac_key_resp.rt = undefined;
    _instruction_prac_key_resp_allKeys = [];
    // keep track of which components have finished
    instruction_pracComponents = [];
    instruction_pracComponents.push(instruction_prac_image);
    instruction_pracComponents.push(instruction_prac_key_resp);
    
    for (const thisComponent of instruction_pracComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}

function instruction_pracRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'instruction_prac' ---
    // get current time
    t = instruction_pracClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *instruction_prac_image* updates
    if (t >= 0.0 && instruction_prac_image.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      instruction_prac_image.tStart = t;  // (not accounting for frame time here)
      instruction_prac_image.frameNStart = frameN;  // exact frame index
      
      instruction_prac_image.setAutoDraw(true);
    }

    
    // *instruction_prac_key_resp* updates
    if (t >= 0.0 && instruction_prac_key_resp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      instruction_prac_key_resp.tStart = t;  // (not accounting for frame time here)
      instruction_prac_key_resp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { instruction_prac_key_resp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { instruction_prac_key_resp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { instruction_prac_key_resp.clearEvents(); });
    }

    if (instruction_prac_key_resp.status === PsychoJS.Status.STARTED) {
      let theseKeys = instruction_prac_key_resp.getKeys({keyList: ['space'], waitRelease: false});
      _instruction_prac_key_resp_allKeys = _instruction_prac_key_resp_allKeys.concat(theseKeys);
      if (_instruction_prac_key_resp_allKeys.length > 0) {
        instruction_prac_key_resp.keys = _instruction_prac_key_resp_allKeys[_instruction_prac_key_resp_allKeys.length - 1].name;  // just the last key pressed
        instruction_prac_key_resp.rt = _instruction_prac_key_resp_allKeys[_instruction_prac_key_resp_allKeys.length - 1].rt;
        instruction_prac_key_resp.duration = _instruction_prac_key_resp_allKeys[_instruction_prac_key_resp_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of instruction_pracComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}

function instruction_pracRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'instruction_prac' ---
    for (const thisComponent of instruction_pracComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(instruction_prac_key_resp.corr, level);
    }
    psychoJS.experiment.addData('instruction_prac_key_resp.keys', instruction_prac_key_resp.keys);
    if (typeof instruction_prac_key_resp.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('instruction_prac_key_resp.rt', instruction_prac_key_resp.rt);
        psychoJS.experiment.addData('instruction_prac_key_resp.duration', instruction_prac_key_resp.duration);
        routineTimer.reset();
        }
    
    instruction_prac_key_resp.stop();
    // the Routine "instruction_prac" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}

function prac_trialsLoopBegin(prac_trialsLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    prac_trials = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: 'exp_condi_pra.xlsx',
      seed: undefined, name: 'prac_trials'
    });
    psychoJS.experiment.addLoop(prac_trials); // add the loop to the experiment
    currentLoop = prac_trials;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisPrac_trial of prac_trials) {
      snapshot = prac_trials.getSnapshot();
      prac_trialsLoopScheduler.add(importConditions(snapshot));
      prac_trialsLoopScheduler.add(chargeRoutineBegin(snapshot));
      prac_trialsLoopScheduler.add(chargeRoutineEachFrame());
      prac_trialsLoopScheduler.add(chargeRoutineEnd(snapshot));
      prac_trialsLoopScheduler.add(trialRoutineBegin(snapshot));
      prac_trialsLoopScheduler.add(trialRoutineEachFrame());
      prac_trialsLoopScheduler.add(trialRoutineEnd(snapshot));
      prac_trialsLoopScheduler.add(feedbackRoutineBegin(snapshot));
      prac_trialsLoopScheduler.add(feedbackRoutineEachFrame());
      prac_trialsLoopScheduler.add(feedbackRoutineEnd(snapshot));
      prac_trialsLoopScheduler.add(assessmentRoutineBegin(snapshot));
      prac_trialsLoopScheduler.add(assessmentRoutineEachFrame());
      prac_trialsLoopScheduler.add(assessmentRoutineEnd(snapshot));
      prac_trialsLoopScheduler.add(earnedRoutineBegin(snapshot));
      prac_trialsLoopScheduler.add(earnedRoutineEachFrame());
      prac_trialsLoopScheduler.add(earnedRoutineEnd(snapshot));
      prac_trialsLoopScheduler.add(prac_trialsLoopEndIteration(prac_trialsLoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}

async function prac_trialsLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(prac_trials);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}

function prac_trialsLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}

function trialsLoopBegin(trialsLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    trials = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
      extraInfo: expInfo, originPath: undefined,
      trialList: 'exp_condi_H.xlsx',
      seed: undefined, name: 'trials'
    });
    psychoJS.experiment.addLoop(trials); // add the loop to the experiment
    currentLoop = trials;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisTrial of trials) {
      snapshot = trials.getSnapshot();
      trialsLoopScheduler.add(importConditions(snapshot));
      trialsLoopScheduler.add(chargeRoutineBegin(snapshot));
      trialsLoopScheduler.add(chargeRoutineEachFrame());
      trialsLoopScheduler.add(chargeRoutineEnd(snapshot));
      trialsLoopScheduler.add(trialRoutineBegin(snapshot));
      trialsLoopScheduler.add(trialRoutineEachFrame());
      trialsLoopScheduler.add(trialRoutineEnd(snapshot));
      trialsLoopScheduler.add(feedbackRoutineBegin(snapshot));
      trialsLoopScheduler.add(feedbackRoutineEachFrame());
      trialsLoopScheduler.add(feedbackRoutineEnd(snapshot));
      trialsLoopScheduler.add(assessmentRoutineBegin(snapshot));
      trialsLoopScheduler.add(assessmentRoutineEachFrame());
      trialsLoopScheduler.add(assessmentRoutineEnd(snapshot));
      trialsLoopScheduler.add(earnedRoutineBegin(snapshot));
      trialsLoopScheduler.add(earnedRoutineEachFrame());
      trialsLoopScheduler.add(earnedRoutineEnd(snapshot));
      trialsLoopScheduler.add(trialsLoopEndIteration(trialsLoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}

async function trialsLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(trials);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}

function trialsLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}

function trials_2LoopBegin(trials_2LoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    trials_2 = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
      extraInfo: expInfo, originPath: undefined,
      trialList: 'exp_condi_L.xlsx',
      seed: undefined, name: 'trials_2'
    });
    psychoJS.experiment.addLoop(trials_2); // add the loop to the experiment
    currentLoop = trials_2;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisTrial_2 of trials_2) {
      snapshot = trials_2.getSnapshot();
      trials_2LoopScheduler.add(importConditions(snapshot));
      trials_2LoopScheduler.add(chargeRoutineBegin(snapshot));
      trials_2LoopScheduler.add(chargeRoutineEachFrame());
      trials_2LoopScheduler.add(chargeRoutineEnd(snapshot));
      trials_2LoopScheduler.add(trialRoutineBegin(snapshot));
      trials_2LoopScheduler.add(trialRoutineEachFrame());
      trials_2LoopScheduler.add(trialRoutineEnd(snapshot));
      trials_2LoopScheduler.add(feedbackRoutineBegin(snapshot));
      trials_2LoopScheduler.add(feedbackRoutineEachFrame());
      trials_2LoopScheduler.add(feedbackRoutineEnd(snapshot));
      trials_2LoopScheduler.add(assessmentRoutineBegin(snapshot));
      trials_2LoopScheduler.add(assessmentRoutineEachFrame());
      trials_2LoopScheduler.add(assessmentRoutineEnd(snapshot));
      trials_2LoopScheduler.add(earnedRoutineBegin(snapshot));
      trials_2LoopScheduler.add(earnedRoutineEachFrame());
      trials_2LoopScheduler.add(earnedRoutineEnd(snapshot));
      trials_2LoopScheduler.add(trials_2LoopEndIteration(trials_2LoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}

async function trials_2LoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(trials_2);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}

function trials_2LoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}

function chargeRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'charge' ---
    t = 0;
    chargeClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    // Run 'Begin Routine' code from charge_code
    tmp_invest = 1;
    safe_account_text = ("\u5b89\u5168\u8d26\u6237\uff1a" + safe_account.toString());
    
    charge_slider.reset()
    charge_image.setImage('charge_image.jpg');
    account_text.setText(safe_account_text);
    // reset charge_button to account for continued clicks & clear times on/off
    charge_button.reset()
    // keep track of which components have finished
    chargeComponents = [];
    chargeComponents.push(charge_slider);
    chargeComponents.push(charge_image);
    chargeComponents.push(account_text);
    chargeComponents.push(charge_button);
    
    for (const thisComponent of chargeComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}

function chargeRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'charge' ---
    // get current time
    t = chargeClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    // Run 'Each Frame' code from charge_code
    if ((charge_slider.getRating() === null)) {
        tmp_invest = 1;
    } else {
        tmp_invest = Number.parseInt(charge_slider.getRating());
    }
    tmp_invest_text = tmp_invest.toString();
    
    
    // *charge_slider* updates
    if (t >= 0.0 && charge_slider.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      charge_slider.tStart = t;  // (not accounting for frame time here)
      charge_slider.frameNStart = frameN;  // exact frame index
      
      charge_slider.setAutoDraw(true);
    }

    
    // *charge_image* updates
    if (t >= 0.0 && charge_image.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      charge_image.tStart = t;  // (not accounting for frame time here)
      charge_image.frameNStart = frameN;  // exact frame index
      
      charge_image.setAutoDraw(true);
    }

    
    // *account_text* updates
    if (t >= 0.0 && account_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      account_text.tStart = t;  // (not accounting for frame time here)
      account_text.frameNStart = frameN;  // exact frame index
      
      account_text.setAutoDraw(true);
    }

    
    // *charge_button* updates
    if (t >= 0 && charge_button.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      charge_button.tStart = t;  // (not accounting for frame time here)
      charge_button.frameNStart = frameN;  // exact frame index
      
      charge_button.setAutoDraw(true);
    }

    
    if (charge_button.status === PsychoJS.Status.STARTED){ // only update if being drawn
      charge_button.setText(tmp_invest_text, false);
    }
    if (charge_button.status === PsychoJS.Status.STARTED) {
      // check whether charge_button has been pressed
      if (charge_button.isClicked) {
        if (!charge_button.wasClicked) {
          // store time of first click
          charge_button.timesOn.push(charge_button.clock.getTime());
          charge_button.numClicks += 1;
          // store time clicked until
          charge_button.timesOff.push(charge_button.clock.getTime());
        } else {
          // update time clicked until;
          charge_button.timesOff[charge_button.timesOff.length - 1] = charge_button.clock.getTime();
        }
        if (!charge_button.wasClicked) {
          // end routine when charge_button is clicked
          continueRoutine = false;
        }
        // if charge_button is still clicked next frame, it is not a new click
        charge_button.wasClicked = true;
      } else {
        // if charge_button is clicked next frame, it is a new click
        charge_button.wasClicked = false;
      }
    } else {
      // keep clock at 0 if charge_button hasn't started / has finished
      charge_button.clock.reset();
      // if charge_button is clicked next frame, it is a new click
      charge_button.wasClicked = false;
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of chargeComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}

function chargeRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'charge' ---
    for (const thisComponent of chargeComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('charge_slider.response', charge_slider.getRating());
    psychoJS.experiment.addData('charge_button.numClicks', charge_button.numClicks);
    psychoJS.experiment.addData('charge_button.timesOn', charge_button.timesOn);
    psychoJS.experiment.addData('charge_button.timesOff', charge_button.timesOff);
    // the Routine "charge" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}

function trialRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'trial' ---
    t = 0;
    trialClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    // Run 'Begin Routine' code from trial_code
    balloonSize = initSize;
    popped = false;
    nPumps = 0;
    nVal = 0;
    inval_in = 0;
    noExpandList = [r1, r2, r3];
    psychoJS.eventManager.clearEvents();
    if ((expInfo["exp_type"] === "prac")) {
        reminder = "\u6309\u7a7a\u683c\u952e\u5145\u6c14\n\u6309\u56de\u8f66\u952e\u4e2d\u6b62";
    } else {
        reminder = `按空格键充气
    按回车键中止
    当前是${(trials_exp.thisTrialN + 1)}轮，共${trials_exp.nTotal}`
    ;
    }
    
    Balloon.setImage('balloon.png');
    reminder_text.setText('按空格键充气\n按回车键中止');
    safeaccount_text.setText(safe_account_text);
    investaccount_text.setText(invest_account_text);
    bankButton_key_resp.keys = undefined;
    bankButton_key_resp.rt = undefined;
    _bankButton_key_resp_allKeys = [];
    text.setText(tri_msg);
    // keep track of which components have finished
    trialComponents = [];
    trialComponents.push(Balloon);
    trialComponents.push(reminder_text);
    trialComponents.push(safeaccount_text);
    trialComponents.push(investaccount_text);
    trialComponents.push(bankButton_key_resp);
    trialComponents.push(pumpwarning_text);
    trialComponents.push(text);
    
    for (const thisComponent of trialComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}

function trialRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'trial' ---
    // get current time
    t = trialClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *Balloon* updates
    if (t >= 0.0 && Balloon.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Balloon.tStart = t;  // (not accounting for frame time here)
      Balloon.frameNStart = frameN;  // exact frame index
      
      Balloon.setAutoDraw(true);
    }

    
    if (Balloon.status === PsychoJS.Status.STARTED){ // only update if being drawn
      Balloon.setSize([balloonSize, (balloonSize * 2.2)], false);
    }
    
    // *reminder_text* updates
    if (t >= 0.0 && reminder_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      reminder_text.tStart = t;  // (not accounting for frame time here)
      reminder_text.frameNStart = frameN;  // exact frame index
      
      reminder_text.setAutoDraw(true);
    }

    
    // *safeaccount_text* updates
    if (t >= 0.0 && safeaccount_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      safeaccount_text.tStart = t;  // (not accounting for frame time here)
      safeaccount_text.frameNStart = frameN;  // exact frame index
      
      safeaccount_text.setAutoDraw(true);
    }

    
    // *investaccount_text* updates
    if (t >= 0.0 && investaccount_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      investaccount_text.tStart = t;  // (not accounting for frame time here)
      investaccount_text.frameNStart = frameN;  // exact frame index
      
      investaccount_text.setAutoDraw(true);
    }

    
    // *bankButton_key_resp* updates
    if (t >= 0.0 && bankButton_key_resp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      bankButton_key_resp.tStart = t;  // (not accounting for frame time here)
      bankButton_key_resp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { bankButton_key_resp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { bankButton_key_resp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { bankButton_key_resp.clearEvents(); });
    }

    if (bankButton_key_resp.status === PsychoJS.Status.STARTED) {
      let theseKeys = bankButton_key_resp.getKeys({keyList: ['return'], waitRelease: false});
      _bankButton_key_resp_allKeys = _bankButton_key_resp_allKeys.concat(theseKeys);
      if (_bankButton_key_resp_allKeys.length > 0) {
        bankButton_key_resp.keys = _bankButton_key_resp_allKeys[_bankButton_key_resp_allKeys.length - 1].name;  // just the last key pressed
        bankButton_key_resp.rt = _bankButton_key_resp_allKeys[_bankButton_key_resp_allKeys.length - 1].rt;
        bankButton_key_resp.duration = _bankButton_key_resp_allKeys[_bankButton_key_resp_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *pumpwarning_text* updates
    if (t >= 0.0 && pumpwarning_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      pumpwarning_text.tStart = t;  // (not accounting for frame time here)
      pumpwarning_text.frameNStart = frameN;  // exact frame index
      
      pumpwarning_text.setAutoDraw(true);
    }

    
    if (pumpwarning_text.status === PsychoJS.Status.STARTED){ // only update if being drawn
      pumpwarning_text.setText(pum_msg, false);
    }
    
    // *text* updates
    if (((tri_num > 3)) && text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text.tStart = t;  // (not accounting for frame time here)
      text.frameNStart = frameN;  // exact frame index
      
      text.setAutoDraw(true);
    }

    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of trialComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}

function trialRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'trial' ---
    for (const thisComponent of trialComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(bankButton_key_resp.corr, level);
    }
    psychoJS.experiment.addData('bankButton_key_resp.keys', bankButton_key_resp.keys);
    if (typeof bankButton_key_resp.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('bankButton_key_resp.rt', bankButton_key_resp.rt);
        psychoJS.experiment.addData('bankButton_key_resp.duration', bankButton_key_resp.duration);
        routineTimer.reset();
        }
    
    bankButton_key_resp.stop();
    // the Routine "trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}

function feedbackRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'feedback' ---
    t = 0;
    feedbackClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    // Run 'Begin Routine' code from feedback_code
    psychoJS.eventManager.clearEvents();
    stateSize = initSize;
    stateImage = crackImageFile;
    if ((popped === true)) {
        if ((Number.parseInt(probas) === 1)) {
            feedbackText = (((("\u5728\u7b2c" + lossPoint.toString()) + "\u4e2a\u4ea4\u6613\u65e5\u540e\uff0c\u6c14\u7403\u70b8\u4e86\uff01\n\u4f60\u7684\u6536\u76ca\u4e3a:") + tmp_profit.toString()) + "\n\u8bf7\u6309\u56de\u8f66\u952e\u7ee7\u7eed");
            bang.play();
        } else {
            stateImage = imageFile;
            feedbackText = (((("\u5728\u7b2c" + lossPoint.toString()) + "\u4e2a\u4ea4\u6613\u65e5\u540e\uff0c\u6c14\u7403\u6f0f\u6c14\u4e86\uff01\n\u4f60\u7684\u6536\u76ca\u4e3a:") + tmp_profit.toString()) + "\n\u8bf7\u6309\u56de\u8f66\u952e\u7ee7\u7eed");
            leaky.play();
        }
    } else {
        feedbackText = (((("\u6c14\u7403\u5c06\u5728\u7b2c" + lossPoint.toString()) + "\u4e2a\u4ea4\u6613\u65e5\u540e\u7206\u70b8/\u6f0f\u6c14\uff0c\n\u4f60\u7684\u6536\u76ca\u4e3a:") + tmp_profit.toString()) + "\n\u8bf7\u6309\u56de\u8f66\u952e\u7ee7\u7eed");
        stateSize = balloonSize;
        stateImage = imageFile;
    }
    
    feedback_image.setImage(stateImage);
    feedback_text.setText(feedbackText);
    feedback_key_resp.keys = undefined;
    feedback_key_resp.rt = undefined;
    _feedback_key_resp_allKeys = [];
    // keep track of which components have finished
    feedbackComponents = [];
    feedbackComponents.push(feedback_image);
    feedbackComponents.push(feedback_text);
    feedbackComponents.push(feedback_key_resp);
    
    for (const thisComponent of feedbackComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}

function feedbackRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'feedback' ---
    // get current time
    t = feedbackClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *feedback_image* updates
    if (t >= 0.0 && feedback_image.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      feedback_image.tStart = t;  // (not accounting for frame time here)
      feedback_image.frameNStart = frameN;  // exact frame index
      
      feedback_image.setAutoDraw(true);
    }

    
    // *feedback_text* updates
    if (t >= 0.0 && feedback_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      feedback_text.tStart = t;  // (not accounting for frame time here)
      feedback_text.frameNStart = frameN;  // exact frame index
      
      feedback_text.setAutoDraw(true);
    }

    
    // *feedback_key_resp* updates
    if (t >= 0.0 && feedback_key_resp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      feedback_key_resp.tStart = t;  // (not accounting for frame time here)
      feedback_key_resp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { feedback_key_resp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { feedback_key_resp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { feedback_key_resp.clearEvents(); });
    }

    if (feedback_key_resp.status === PsychoJS.Status.STARTED) {
      let theseKeys = feedback_key_resp.getKeys({keyList: ['return'], waitRelease: false});
      _feedback_key_resp_allKeys = _feedback_key_resp_allKeys.concat(theseKeys);
      if (_feedback_key_resp_allKeys.length > 0) {
        feedback_key_resp.keys = _feedback_key_resp_allKeys[_feedback_key_resp_allKeys.length - 1].name;  // just the last key pressed
        feedback_key_resp.rt = _feedback_key_resp_allKeys[_feedback_key_resp_allKeys.length - 1].rt;
        feedback_key_resp.duration = _feedback_key_resp_allKeys[_feedback_key_resp_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of feedbackComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}

function feedbackRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'feedback' ---
    for (const thisComponent of feedbackComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(feedback_key_resp.corr, level);
    }
    psychoJS.experiment.addData('feedback_key_resp.keys', feedback_key_resp.keys);
    if (typeof feedback_key_resp.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('feedback_key_resp.rt', feedback_key_resp.rt);
        psychoJS.experiment.addData('feedback_key_resp.duration', feedback_key_resp.duration);
        routineTimer.reset();
        }
    
    feedback_key_resp.stop();
    // the Routine "feedback" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}

function assessmentRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'assessment' ---
    t = 0;
    assessmentClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    assessment_text.setText('本轮投资结束，看到收益结果后，\n如果感到后悔，请您评价自己的后悔程度\n（1表示稍微有点后悔，7表示非常后悔）');
    assessment_image.setImage('assessment_image.jpg');
    assessment_slider.reset()
    // keep track of which components have finished
    assessmentComponents = [];
    assessmentComponents.push(assessment_text);
    assessmentComponents.push(assessment_image);
    assessmentComponents.push(assessment_slider);
    
    for (const thisComponent of assessmentComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}

function assessmentRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'assessment' ---
    // get current time
    t = assessmentClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *assessment_text* updates
    if (t >= 0.0 && assessment_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      assessment_text.tStart = t;  // (not accounting for frame time here)
      assessment_text.frameNStart = frameN;  // exact frame index
      
      assessment_text.setAutoDraw(true);
    }

    
    // *assessment_image* updates
    if (t >= 0.0 && assessment_image.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      assessment_image.tStart = t;  // (not accounting for frame time here)
      assessment_image.frameNStart = frameN;  // exact frame index
      
      assessment_image.setAutoDraw(true);
    }

    
    // *assessment_slider* updates
    if (t >= 0.0 && assessment_slider.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      assessment_slider.tStart = t;  // (not accounting for frame time here)
      assessment_slider.frameNStart = frameN;  // exact frame index
      
      assessment_slider.setAutoDraw(true);
    }

    
    // Check assessment_slider for response to end routine
    if (assessment_slider.getRating() !== undefined && assessment_slider.status === PsychoJS.Status.STARTED) {
      continueRoutine = false; }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of assessmentComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}

function assessmentRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'assessment' ---
    for (const thisComponent of assessmentComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('assessment_slider.response', assessment_slider.getRating());
    // the Routine "assessment" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}

function earnedRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'earned' ---
    t = 0;
    earnedClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    // Run 'Begin Routine' code from earned_code
    psychoJS.eventManager.clearEvents();
    tip_text = "";
    if ((period === 0)) {
        if ((prac_trials.thisTrialN === 2)) {
            continueRoutine = true;
            tip_text = `您已经进行了${(prac_trials.thisTrialN + 1)}次实验，最终收益为：${safe_account}`;
            prac_trials.finished = true;
        } else {
            continueRoutine = false;
        }
    } else {
        if ((trials.thisTrialN === (trials.nTotal - 1))) {
            continueRoutine = true;
            tip_text = `您已经进行了${(trials.thisTrialN + 1)}次实验，最终收益为：${safe_account}`;
            trials.finished = true;
        } else {
            continueRoutine = false;
        }
    }
    
    earned_text.setText(tip_text);
    earned_key_resp.keys = undefined;
    earned_key_resp.rt = undefined;
    _earned_key_resp_allKeys = [];
    // keep track of which components have finished
    earnedComponents = [];
    earnedComponents.push(earned_text);
    earnedComponents.push(earned_key_resp);
    
    for (const thisComponent of earnedComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}

function earnedRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'earned' ---
    // get current time
    t = earnedClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *earned_text* updates
    if (t >= 0.0 && earned_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      earned_text.tStart = t;  // (not accounting for frame time here)
      earned_text.frameNStart = frameN;  // exact frame index
      
      earned_text.setAutoDraw(true);
    }

    
    // *earned_key_resp* updates
    if (t >= 0.0 && earned_key_resp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      earned_key_resp.tStart = t;  // (not accounting for frame time here)
      earned_key_resp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      earned_key_resp.clock.reset();
      earned_key_resp.start();
    }

    if (earned_key_resp.status === PsychoJS.Status.STARTED) {
      let theseKeys = earned_key_resp.getKeys({keyList: ['space'], waitRelease: false});
      _earned_key_resp_allKeys = _earned_key_resp_allKeys.concat(theseKeys);
      if (_earned_key_resp_allKeys.length > 0) {
        earned_key_resp.keys = _earned_key_resp_allKeys[_earned_key_resp_allKeys.length - 1].name;  // just the last key pressed
        earned_key_resp.rt = _earned_key_resp_allKeys[_earned_key_resp_allKeys.length - 1].rt;
        earned_key_resp.duration = _earned_key_resp_allKeys[_earned_key_resp_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of earnedComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}

function earnedRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'earned' ---
    for (const thisComponent of earnedComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(earned_key_resp.corr, level);
    }
    psychoJS.experiment.addData('earned_key_resp.keys', earned_key_resp.keys);
    if (typeof earned_key_resp.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('earned_key_resp.rt', earned_key_resp.rt);
        psychoJS.experiment.addData('earned_key_resp.duration', earned_key_resp.duration);
        routineTimer.reset();
        }
    
    earned_key_resp.stop();
    // the Routine "earned" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}

function formal_intro2RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'formal_intro2' ---
    t = 0;
    formal_intro2Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    formal_intro_key_resp.keys = undefined;
    formal_intro_key_resp.rt = undefined;
    _formal_intro_key_resp_allKeys = [];
    // keep track of which components have finished
    formal_intro2Components = [];
    formal_intro2Components.push(formal_intro_image);
    formal_intro2Components.push(formal_intro_key_resp);
    
    for (const thisComponent of formal_intro2Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}

function formal_intro2RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'formal_intro2' ---
    // get current time
    t = formal_intro2Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *formal_intro_image* updates
    if (t >= 0.0 && formal_intro_image.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      formal_intro_image.tStart = t;  // (not accounting for frame time here)
      formal_intro_image.frameNStart = frameN;  // exact frame index
      
      formal_intro_image.setAutoDraw(true);
    }

    
    // *formal_intro_key_resp* updates
    if (t >= 0.0 && formal_intro_key_resp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      formal_intro_key_resp.tStart = t;  // (not accounting for frame time here)
      formal_intro_key_resp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { formal_intro_key_resp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { formal_intro_key_resp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { formal_intro_key_resp.clearEvents(); });
    }

    if (formal_intro_key_resp.status === PsychoJS.Status.STARTED) {
      let theseKeys = formal_intro_key_resp.getKeys({keyList: ['space'], waitRelease: false});
      _formal_intro_key_resp_allKeys = _formal_intro_key_resp_allKeys.concat(theseKeys);
      if (_formal_intro_key_resp_allKeys.length > 0) {
        formal_intro_key_resp.keys = _formal_intro_key_resp_allKeys[_formal_intro_key_resp_allKeys.length - 1].name;  // just the last key pressed
        formal_intro_key_resp.rt = _formal_intro_key_resp_allKeys[_formal_intro_key_resp_allKeys.length - 1].rt;
        formal_intro_key_resp.duration = _formal_intro_key_resp_allKeys[_formal_intro_key_resp_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of formal_intro2Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}

function formal_intro2RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'formal_intro2' ---
    for (const thisComponent of formal_intro2Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(formal_intro_key_resp.corr, level);
    }
    psychoJS.experiment.addData('formal_intro_key_resp.keys', formal_intro_key_resp.keys);
    if (typeof formal_intro_key_resp.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('formal_intro_key_resp.rt', formal_intro_key_resp.rt);
        psychoJS.experiment.addData('formal_intro_key_resp.duration', formal_intro_key_resp.duration);
        routineTimer.reset();
        }
    
    formal_intro_key_resp.stop();
    // the Routine "formal_intro2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}

function instructionsRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'instructions' ---
    t = 0;
    instructionsClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    // Run 'Begin Routine' code from intro_code
    safe_account = Number.parseFloat(`${0.0}`);
    
    instructions_key_resp.keys = undefined;
    instructions_key_resp.rt = undefined;
    _instructions_key_resp_allKeys = [];
    // keep track of which components have finished
    instructionsComponents = [];
    instructionsComponents.push(formal_image);
    instructionsComponents.push(instructions_key_resp);
    
    for (const thisComponent of instructionsComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}

function instructionsRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'instructions' ---
    // get current time
    t = instructionsClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *formal_image* updates
    if (t >= 0.0 && formal_image.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      formal_image.tStart = t;  // (not accounting for frame time here)
      formal_image.frameNStart = frameN;  // exact frame index
      
      formal_image.setAutoDraw(true);
    }

    
    // *instructions_key_resp* updates
    if (t >= 0.0 && instructions_key_resp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      instructions_key_resp.tStart = t;  // (not accounting for frame time here)
      instructions_key_resp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { instructions_key_resp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { instructions_key_resp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { instructions_key_resp.clearEvents(); });
    }

    if (instructions_key_resp.status === PsychoJS.Status.STARTED) {
      let theseKeys = instructions_key_resp.getKeys({keyList: ['space'], waitRelease: false});
      _instructions_key_resp_allKeys = _instructions_key_resp_allKeys.concat(theseKeys);
      if (_instructions_key_resp_allKeys.length > 0) {
        instructions_key_resp.keys = _instructions_key_resp_allKeys[_instructions_key_resp_allKeys.length - 1].name;  // just the last key pressed
        instructions_key_resp.rt = _instructions_key_resp_allKeys[_instructions_key_resp_allKeys.length - 1].rt;
        instructions_key_resp.duration = _instructions_key_resp_allKeys[_instructions_key_resp_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of instructionsComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}

function instructionsRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'instructions' ---
    for (const thisComponent of instructionsComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(instructions_key_resp.corr, level);
    }
    psychoJS.experiment.addData('instructions_key_resp.keys', instructions_key_resp.keys);
    if (typeof instructions_key_resp.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('instructions_key_resp.rt', instructions_key_resp.rt);
        psychoJS.experiment.addData('instructions_key_resp.duration', instructions_key_resp.duration);
        routineTimer.reset();
        }
    
    instructions_key_resp.stop();
    // the Routine "instructions" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}

function relaxRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'relax' ---
    t = 0;
    relaxClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    // Run 'Begin Routine' code from code
    safe_account = Number.parseFloat(`${0.0}`);
    
    relax_key_resp.keys = undefined;
    relax_key_resp.rt = undefined;
    _relax_key_resp_allKeys = [];
    // keep track of which components have finished
    relaxComponents = [];
    relaxComponents.push(relax_key_resp);
    relaxComponents.push(relax_image);
    relaxComponents.push(clock_movie);
    
    for (const thisComponent of relaxComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}

function relaxRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'relax' ---
    // get current time
    t = relaxClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *relax_key_resp* updates
    if (t >= 30 && relax_key_resp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      relax_key_resp.tStart = t;  // (not accounting for frame time here)
      relax_key_resp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { relax_key_resp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { relax_key_resp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { relax_key_resp.clearEvents(); });
    }

    if (relax_key_resp.status === PsychoJS.Status.STARTED) {
      let theseKeys = relax_key_resp.getKeys({keyList: ['space'], waitRelease: false});
      _relax_key_resp_allKeys = _relax_key_resp_allKeys.concat(theseKeys);
      if (_relax_key_resp_allKeys.length > 0) {
        relax_key_resp.keys = _relax_key_resp_allKeys[_relax_key_resp_allKeys.length - 1].name;  // just the last key pressed
        relax_key_resp.rt = _relax_key_resp_allKeys[_relax_key_resp_allKeys.length - 1].rt;
        relax_key_resp.duration = _relax_key_resp_allKeys[_relax_key_resp_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *relax_image* updates
    if (t >= 0.0 && relax_image.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      relax_image.tStart = t;  // (not accounting for frame time here)
      relax_image.frameNStart = frameN;  // exact frame index
      
      relax_image.setAutoDraw(true);
    }

    
    // *clock_movie* updates
    if (t >= 0.0 && clock_movie.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      clock_movie.tStart = t;  // (not accounting for frame time here)
      clock_movie.frameNStart = frameN;  // exact frame index
      
      clock_movie.setAutoDraw(true);
      clock_movie.play();
    }

    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of relaxComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}

function relaxRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'relax' ---
    for (const thisComponent of relaxComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(relax_key_resp.corr, level);
    }
    psychoJS.experiment.addData('relax_key_resp.keys', relax_key_resp.keys);
    if (typeof relax_key_resp.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('relax_key_resp.rt', relax_key_resp.rt);
        psychoJS.experiment.addData('relax_key_resp.duration', relax_key_resp.duration);
        routineTimer.reset();
        }
    
    relax_key_resp.stop();
    clock_movie.stop();
    // the Routine "relax" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}

function endingRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'ending' ---
    t = 0;
    endingClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    ending_key_resp.keys = undefined;
    ending_key_resp.rt = undefined;
    _ending_key_resp_allKeys = [];
    // keep track of which components have finished
    endingComponents = [];
    endingComponents.push(ending_image);
    endingComponents.push(ending_key_resp);
    
    for (const thisComponent of endingComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}

function endingRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'ending' ---
    // get current time
    t = endingClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *ending_image* updates
    if (t >= 0.0 && ending_image.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      ending_image.tStart = t;  // (not accounting for frame time here)
      ending_image.frameNStart = frameN;  // exact frame index
      
      ending_image.setAutoDraw(true);
    }

    
    // *ending_key_resp* updates
    if (t >= 0.0 && ending_key_resp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      ending_key_resp.tStart = t;  // (not accounting for frame time here)
      ending_key_resp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      ending_key_resp.clock.reset();
      ending_key_resp.start();
    }

    if (ending_key_resp.status === PsychoJS.Status.STARTED) {
      let theseKeys = ending_key_resp.getKeys({keyList: ['space'], waitRelease: false});
      _ending_key_resp_allKeys = _ending_key_resp_allKeys.concat(theseKeys);
      if (_ending_key_resp_allKeys.length > 0) {
        ending_key_resp.keys = _ending_key_resp_allKeys[_ending_key_resp_allKeys.length - 1].name;  // just the last key pressed
        ending_key_resp.rt = _ending_key_resp_allKeys[_ending_key_resp_allKeys.length - 1].rt;
        ending_key_resp.duration = _ending_key_resp_allKeys[_ending_key_resp_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of endingComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}

function endingRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'ending' ---
    for (const thisComponent of endingComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    ending_key_resp.stop();
    // the Routine "ending" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}

function importConditions(currentLoop) {
  return async function () {
    psychoJS.importAttributes(currentLoop.getCurrentTrial());
    return Scheduler.Event.NEXT;
    };
}

async function quitPsychoJS(message, isCompleted) {
  // Check for and save orphaned data
  if (psychoJS.experiment.isEntryEmpty()) {
    psychoJS.experiment.nextEntry();
  }
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  psychoJS.window.close();
  psychoJS.quit({message: message, isCompleted: isCompleted});
  
  return Scheduler.Event.QUIT;
}
