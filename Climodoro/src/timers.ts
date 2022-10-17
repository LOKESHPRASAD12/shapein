export class Watch {
  private intervalID: any = null;
  private counter = 1;
  constructor(private fns: {onStart: any, onEnd: any} ) {}

  start() {
    this.intervalID = setInterval(() => {
      this.fns.onStart(this.counter);
      this.counter += 1;
    }, 1000)
  }

  stop() {
    clearInterval(this.intervalID);
    this.intervalID = null;
    this.fns.onEnd();
  }
}

export class Timer {
  private intervalID: any = null;
  public totalSeconds: number = 0;
  constructor(private fns: {onStart: any, onEnd: any, onProgress: any}, private secondsRemaining: number ) {}

  start() {
    let counter = this.secondsRemaining;
    this.fns.onStart();
    this.intervalID = setInterval(() => {
      this.fns.onProgress(counter);
      if (counter <= 1) this.stop();
      counter -= 1;
      this.totalSeconds += 1;
    }, 1000)
  }

  stop() {
    clearInterval(this.intervalID);
    this.intervalID = null;
    this.fns.onEnd();
  }

  forceStop() {
    clearInterval(this.intervalID);
    this.intervalID = null;
  }
}