import winston from 'winston';

let env = process.env.NODE_ENV || 'development';

let logger_choice;

if (env === "test") {
  logger_choice = winston.createLogger({
    silent: true,
  })
} else {
  logger_choice = winston.createLogger({
    level: 'verbose',
    format: winston.format.combine(
      winston.format.timestamp(),
      winston.format.json()),
    transports: [
      new winston.transports.Console(),
      new winston.transports.File({ filename: 'error.log', level: 'error' }),
      new winston.transports.File({ filename: 'http.log', level: 'http' }),
    ],
  });
}

export const logger = logger_choice;