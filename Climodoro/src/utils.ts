const appendZero = (num: number): string => (num < 10) ? `0${num}` : `${num}`;
const MILISECONDS = 1000;

export const secondsToTime = (secondsArg: number) => {
  let seconds: any = appendZero(Math.floor(secondsArg % 60));
  let	minutes: any = appendZero(Math.floor((secondsArg / 60) % 60));
  let hours: any = appendZero(Math.floor((secondsArg / (60 * 60)) % 24));

  return `${hours}:${minutes}:${seconds}`;
}

export const UTCDateToTime = (utcDate: string) => {
  const [, hours, minutes, seconds ] = /(\d\d):(\d\d):(\d\d)/.exec(utcDate) as string[];
  return `${hours}:${minutes}:${seconds}`
}

export const secondsToDate = (seconds: number) => new Date(seconds * MILISECONDS);

export const milisecondsToDateString = (miliseconds: number) => {
  const timeReg = /\d{1,2}:\d{1,2}:\d{1,2}/;
  const dateReg = /\d{4}-\d{2}-\d{1,2}/;
  const date = new Date(miliseconds);

  let time: any = timeReg.exec(date.toString());
  time = (time !== null) ?
    time[0]
  :
    "";
  let dateString: any = dateReg.exec(date.toISOString());
  dateString = (time !== null) ?
    dateString[0]
  :
    "";

  return `${dateString} ${time}`;
}