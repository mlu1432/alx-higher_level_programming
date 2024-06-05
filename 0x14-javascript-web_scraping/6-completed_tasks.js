#!/usr/bin/node
// Script computes the number of tasks completed by user id

const request = require('request');
const url = process.argv[2];

request(url, function (err, response, body) {
        if (err) {
                console.error(err);
                return;
        }

        if (response.statusCode !== 200) {
                console.error('An error occurred. Status code:', response.statusCode);
                return;
        }

        const completed = {};
        const tasks = JSON.parse(body);

        tasks.forEach(task => {
                if (task.completed) {
                        if (!completed[task.userId]) {
                                completed[task.userId] = 1;
                        }
                        else {
                                completed[task.userId]++;
                        }
                }
        });

        console.log(completed);
});
