import { app } from "./app.js"

import { logger } from './logger.js';

const hostname = '127.0.0.1';
const port = 3000;


app.listen(port, hostname);
logger.info(`Start server at http://${hostname}:${port}/`)
