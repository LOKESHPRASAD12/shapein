import { showMenu, showTimeLog, showTrackingMenu, showTrackingMenuPomodoro } from './views.js'
import { menuOptions } from './types/index.js';
import { init, disconnect, createLog, getAllLogs } from './data/index.js';
import { secondsToDate, UTCDateToTime } from './utils.js';
import { generateLogReport } from './report/index.js';

let selectedMenu: menuOptions = 'menu';
let totalTime;

(async () => {
  try {
    await init();
    while (true) {
      switch (selectedMenu as any) {
        case 'menu': {
          selectedMenu = await showMenu(totalTime);
          break;
        }
        case 'trackPomodoro': {
          const result = await showTrackingMenuPomodoro();
          selectedMenu = result.selectedOption;
          totalTime = UTCDateToTime(secondsToDate(result.totalTime).toUTCString());
          await createLog(result.totalTime, 'pomodoro');
          break;
        }
        case 'trackTime': {
          const result = await showTrackingMenu();
          selectedMenu = result.selectedOption;
          totalTime = UTCDateToTime(secondsToDate(result.totalTime).toUTCString());
          await createLog(result.totalTime, 'watch');
          break;
        }
        case 'timeLog': {
          const logs = await getAllLogs();
          const result = await showTimeLog(logs);
          selectedMenu = result.selectedOption;
          break;
        }
        case 'exit':
          process.exit(0);
      }
    }
  } catch (error) {
    console.error("Database initialization throw error");
    console.error(error);
  }
  await disconnect();
})()
