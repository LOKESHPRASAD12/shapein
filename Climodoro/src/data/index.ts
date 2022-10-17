import knex, {Knex} from 'knex';
import { DatabaseError } from './errors.js';

import { Log } from './Time.js';

const config: Knex.Config = {
  client: 'sqlite3',
  connection: {
    filename: './data.db'
  }
}

let knexInstance: Knex;

async function createTablesIfNotExists() {
  let exists = await knexInstance.schema.hasTable('log')
    if (!exists) {
      await knexInstance.schema
      .createTable('log', table => {
        table.increments('id');
        table.string('name');
        table.bigInteger('timeTrackedSeconds');
        table.string('type');
        table.date('createdAt');
      })
    }
}

export async function init() {
  knexInstance = knex(config);
  await createTablesIfNotExists();
}

export async function disconnect() {
  await knexInstance.destroy();
}

export async function createLog(seconds: number, type: 'pomodoro' | 'watch', name = 'Working') {
  try {
    await knexInstance<Log>('log').insert({name, timeTrackedSeconds: seconds, createdAt: new Date().getTime(), type});
  } catch {
    throw new DatabaseError();
  }
}

export async function getAllLogs(): Promise<Log[]> {
  try {
    return await knexInstance<Log>('log').select();
  } catch {
    throw new DatabaseError();
  }
}