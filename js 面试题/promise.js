// 三个队列
// Macro Micro 和 stack
// 在看的时候，按照执行深度依次入队列
// Macro 宏任务，有执行源头（setTimeout）

//请写出输出内容
async function async1() {
    console.log('async1 start');
    // async 中 await 前的函数是立即执行的
    await async2();
    // 进入 microtask 队列
    console.log('async1 end');
}
async function async2() {
	console.log('async2');
}

console.log('script start');
// 宏任务源，任务分发到对应队列
setTimeout(function() {
    console.log('setTimeout');
}, 0)

async1();
// promise 中的函数是立即执行的
new Promise(function(resolve) {
    console.log('promise1');
    resolve();
    // 下面异步
}).then(function() {
    console.log('promise2');
});
console.log('script end');


/*
script start
async1 start
async2
promise1
script end
async1 end
promise2
setTimeout
*/


//

async function async1() {
    console.log('async1 start');
    await async2();
    console.log('async1 end');
}
async function async2() {
    //async2做出如下更改：
    new Promise(function(resolve) {
    console.log('promise1');
    resolve();
}).then(function() {
    console.log('promise2');
    });
}
console.log('script start');

setTimeout(function() {
    console.log('setTimeout');
}, 0)
async1();

new Promise(function(resolve) {
    console.log('promise3');
    resolve();
}).then(function() {
    console.log('promise4');
});

console.log('script end');

/*
script start
ayync1 start
promise1
promise3
script end
promise2
async1 end
promise4
timeout jin
*/


/*
script start
async1 start
promise1
script end
promise2
setTimeout3
setTimeout2
setTimeout1

*/