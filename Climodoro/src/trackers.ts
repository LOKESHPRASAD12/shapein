import { createSpinner } from "./spinners.js";
import { Timer, Watch } from "./timers.js";
import { secondsToTime } from "./utils.js";

const SECONDS_MINUTE = 60;

export const startPomodoroTracking = async (fn: any, workMinutes: number, restMinutes: number) => {
  const spinner = createSpinner('red', 'Work time remaining:');
  spinner.start();

  function printProgress(counter: number) {
    spinner.color = 'red';
    spinner.text = `Work time remaining: ${secondsToTime(counter)}`;
  }
  
  function restPrintProgress(counter: number) {
    spinner.color = 'cyan';
    spinner.text = `Rest time remaining: ${secondsToTime(counter)}`
  }
  
  function stopProgress() {
    restTimer.start();
  }

  function stopRest() {
    workTimer.start();
  }

  const workTimer = new Timer({onStart: () => {}, onProgress: printProgress, onEnd: stopProgress}, workMinutes * SECONDS_MINUTE);
  const restTimer = new Timer({onStart: () => {}, onProgress: restPrintProgress, onEnd: stopRest}, restMinutes *  SECONDS_MINUTE);
  workTimer.start()

  const answer = await fn();
  
  workTimer.forceStop();
  restTimer.forceStop();
  spinner.stop();

  return {answer, seconds: workTimer.totalSeconds};
}



export const startWatchTracking = async (fn: any) => {
  const spinnerWatch = createSpinner('cyan', 'Tracking time:');

  function printWatchProgress(counter: number) {
    spinnerWatch.text = `Tracking time: ${secondsToTime(counter)}`
  }

  function stopWatchProgress() {
    spinnerWatch.stop();
  }

  spinnerWatch.start();

  const watch = new Watch({onStart: printWatchProgress, onEnd: stopWatchProgress})
  watch.start()

  let time = new Date().getTime();

  const answer = await fn();

  const difference = new Date().getTime() - time;
  watch.stop();

  return {answer, seconds: (difference / 1000)}
}