import columnify from 'columnify';
import { Log } from '../data/Time.js';
import { milisecondsToDateString, secondsToTime } from '../utils.js';

export function generateLogReport(logs: Log[]) {
  const reportLogs = logs.map(log => ({id: log.id, name: log.name, "Time Tracked": secondsToTime(log.timeTrackedSeconds), "Type Tracking": log.type, "Created At": milisecondsToDateString(log.createdAt)}))
  const columns = [
    "id",
    "name",
    "Time Tracked",
    "Type Tracking",
    "Created At",
  ];

  console.log(columnify(reportLogs, {
    columns
  })
  );
}