export interface Log {
  id: number;
  name: string;
  timeTrackedSeconds: number;
  type: 'pomodoro' | 'watch';
  createdAt: number;
}