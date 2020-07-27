// https://github.com/yisainan/web-interview/blob/master/content/%E5%A4%A7%E5%8E%82%E9%AB%98%E9%A2%91%E9%A2%98.md

// 用深度优先进行拷贝
let cloneObject = function(source){
    // new object
    let target = {}
    // key in source
    for(key in source){
        // if the source has the key
        if (source.hasOwnProperty(key)){
            // clice from 8 to end
            // array, instance of 
            let itemType = Object.prototype.toString.call(source[key]).slice(8, -1)
            switch(itemType){
                case 'Object':
                    target[key] = cloneObject(source[key]);
                    break;
                case "Array":
                    let temp = [];
                    for (let i  = 0; i < source[key].length; i++){
                        temp.push(source[key][i])
                    }
                    target[key] == temp;
                    break;
                default:
                    target[key] = source[key]
            }
        }
    }
    return target
}


// ES5 ES6 的继承除了写法以外还有什么区别

// 数组扁平化

var arr = [ [1, 2, 2], [3, 4, 5, 5], [6, 7, 8, 9, [11, 12, [12, 13, [14] ] ] ], 10];

// a - b < 0 放前面
Array.from(new Set(arr.flat(Infinity))).sort((a, b)=>{
    return a - b
})

// 封装
function fn(time){
    return new Promise(function(resolve){
        setTimeout(function(){
            resolve();
        }, time)
    });
}


let obj = fn(1000)
obj.then()