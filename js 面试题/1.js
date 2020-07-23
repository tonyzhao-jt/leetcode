// 用深度优先进行拷贝
let cloneObject = function(source){
    // new object
    let target = {}
    // key in source
    for(key in source){
        // if the source has the key
        if (source.hasOwnProperty(key)){
            // clice from 8 to end
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
