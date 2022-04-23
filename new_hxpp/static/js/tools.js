//参数:
//obj:要执行动画的对象
//target:执行动画的目标位置
//speed:移动的速度
//attr:要执行动画的样式,比如: left top width height
//callback:回调函数,这个函数将会在动画执行完毕以后执行
function move(obj, attr, target, speed, callback) {
    //关闭上一个定时器
    clearInterval(obj.timer);

    //获取元素目前的位置
    var current = parseInt(getStyle(obj, attr));
    //判断速度的正负值

    if (current > target) {
        //此时速度应为负值
        speed = -speed;
    }

    //开启一个定时器，用来执行动画效果
    obj.timer = setInterval(function () {
        //获取box1的原来的位置值
        var oldValue = parseInt(getStyle(obj, attr));

        //在旧值的基础上增加，值越大越快
        var newValue = oldValue + speed;

        //当元素移动到指定位置时，使其停止执行动画
        //向左移动时,需要判断newValue是否小于target
        //向右移动时,需要判断newValue是否大于target
        if ((speed < 0 && newValue < target) || (speed > 0 && newValue > target)) {
            newValue = target;
        }

        //将新值设置给box1
        obj.style[attr] = newValue + "px";

        //当元素移动到指定位置时,使其停止执行动画
        if (newValue === target) {
            //达到目标,关闭定时器
            clearInterval(obj.timer);
            //动画执行完毕,调用回调函数
            callback && callback();
        }

    }, 20);
};


//getStyle函数：
function getStyle(obj, name) {
    if (window.getComputedStyle) {
        //加上window则为属性，可解决变量全局未定义报错
        //正常浏览器的方式，具有getComputedstyle()方法
        return getComputedStyle(obj, null)[name];
    } else {
        //IE8的方式，不具有getComputedstyle()方法
        return obj.currentStyle[name];
    }
};


//判断一个元素中是否含有指定的class属性值
/*参数:
    obj 要添加class属性的元素
    cn 要判断是否存在的class值
    如果有该class,则返回true,没有则返回false
*/
function hasClass(obj, cn) {
    //判断obj中有没有cn class
    //创建一个正则表达式
    //var reg = /\bb2\b/;				//单词边界	\b
    //但是上面的写死了，需要动态的如下：
    var reg = new RegExp("\\b" + cn + "\\b");

    return reg.test(obj.className);
}


//定义一个函数,用来向一个元素中添加指定的class属性值
/* 参数:
*obj要添加class属性的元素
*cn要添加的class值
*/
function addClass(obj, cn) {

    //检查obj中是否含有cn
    if (!hasClass(obj, cn)) {
        obj.className += " " + cn;
    }

}

function removeClass(obj, cn) {
    //创建一个正则表达式
    var reg = new RegExp("\\b" + cn + "\\b");
    //删除class
    obj.className = obj.className.replace(reg, "");		//替换为空串
}

/*toggleClass可以用来切换一个类
*如果元素中具有该类,则删除
*如果元素中没有该类,则添加
*/
function toggleClass(obj, cn) {
    //判断obj中是否含有cn
    if (hasClass(obj, cn)) {
        //有,则删除
        removeClass(obj, cn);
        //没有,则添加
        addClass(obj, cn);
    }
};



// function adsd() {
//     alert('我是alert')
// }


function AdMove(obj, closeDiv) {
    var timer
    //获取imgdiv
    var imgdiv = document.getElementById(obj)
    //获取closediv
    var closediv = document.getElementById(closeDiv);

    imgdiv.onmouseenter = function () {
        clearInterval(timer);
    }

    closediv.onclick = function () {
        document.getElementById(obj).style.display = "none";
    }

    imgdiv.onmouseleave = function () {
        if (document.getElementById(obj).style.display != "none") {
            timer = setInterval(function () {
                moveadvert(imgdiv, signsplf, signsptp, function () { });
            }, 50)
        }
    }

    var oldValuelef
    var oldValuetop
    // 标示方便计时器接着运行
    var signlf = 0;
    var signtp = 0;
    var signsplf = 0;
    var signsptp = 0;

    timer = setInterval(function () {
        moveadvert(imgdiv, 3, 1, function () { });
    }, 50)

    function moveadvert(obj, speedlef, speedtop, callback) {
        if (signlf != 0 || signtp != 0 || signsplf != 0 || signsptp != 0) {
            oldValuelef = signlf;
            oldValuetop = signtp;
            speedlef = signsplf;
            speedtop = signsptp;
        } else {
            //设置box1的原来的位置值
            oldValuelef = Math.floor(Math.random() * 500);
            oldValuetop = Math.floor(Math.random() * 500);
            obj.style.left = oldValuelef;
            obj.style.top = oldValuetop;
        }

        //在旧值的基础上增加，值越大越快
        var newValuelef = oldValuelef + speedlef;
        var newValuetop = oldValuetop + speedtop;

        if (newValuelef >= $(window).width() + $(document).scrollLeft() - obj.offsetWidth) {
            //此时速度应为负值
            speedlef = -speedlef;
            newValuelef = $(window).width() + $(document).scrollLeft() - obj.offsetWidth;
        } else if (newValuelef <= $(document).scrollLeft()) {
            speedlef = -speedlef;
            newValuelef = $(document).scrollLeft();
        } else { speedlef = speedlef; }

        if (newValuetop >= $(window).height() + $(document).scrollTop() - obj.offsetHeight) {
            //此时速度应为负值
            speedtop = -speedtop;
            newValuetop = $(window).height() + $(document).scrollTop() - obj.offsetHeight;
        } else if (newValuetop <= $(document).scrollTop()) {
            speedtop = -speedtop;
            newValuetop = $(document).scrollTop();
        } else { speedtop = speedtop; }
        // alert()
        // alert("document.body.clientHeight" + document.body.clientHeight + "document.body.clientWidth" + document.body.clientWidth)
        //将新值设置给box1
        obj.style.left = newValuelef + "px";
        obj.style.top = newValuetop + "px";
        // 定时器接着用
        signlf = newValuelef;
        signtp = newValuetop;
        signsplf = speedlef;
        signsptp = speedtop;

    }


};


/**
 * 获取滚动条距离顶端的距离
 * @return {}支持IE6
 */
function getScrollTop() {
    var scrollPos;
    if (window.pageYOffset) {
        scrollPos = window.pageYOffset;
    }
    else if (document.compatMode && document.compatMode != 'BackCompat') { scrollPos = document.documentElement.scrollTop; }
    else if (document.body) { scrollPos = document.body.scrollTop; }
    return scrollPos;
}


//修改当前的标签属性为突出显示
function foo(goal,cont) {
        len1 = goal.length
        for(var i=0;i<len1;i++){
            if(goal[i].text == cont[0].text){
                goal[i].style.cssText = "background:url(../../static/images/shading/mbg.jpg) repeat-x; border:1px solid #dedede;  color:#ff7e00;"

        }
    }
}