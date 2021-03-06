// when the DOM is ready...
$(document).ready(function () {


    // 还不明白具体的作用
    var $panels = $('#slider .scrollContainer > div');
    var $container = $('#slider .scrollContainer');

    // if false, we'll float all the panels left and fix the width 
    // of the container
    var horizontal = false;

    // float the panels left if we're going horizontal
    if (horizontal) {
        $panels.css({
            'float' : 'left',
            'position' : 'relative' // IE fix to ensure overflow is hidden
        });

        // calculate a new width for the container (so it holds all panels)
        $container.css('width', $panels[0].offsetWidth * $panels.length);
    }

    // collect the scroll object, at the same time apply the hidden overflow
    // to remove the default scrollbars that will appear
    var $scroll = $('#slider .scroll').css('overflow', 'hidden');



    // 貌似是接受左右button的
    // apply our left + right buttons
//    $scroll
//        .before('<img class="scrollButtons left" src="" />')
//        .after('<img class="scrollButtons right" src="" />');



    // 导航选择器
    // handle nav selection
    function selectNav() {
        $(this)
            .parents('ul:first')   //找寻到父类空间里ul的第一个li，查找它的标签<a>，移除其class属性     ？？？？？？？？？？？？？？？？？？？？？？
                .find('a')
                    .removeClass('selected')
                .end()
            .end()
            .addClass('selected');    //为当前li下的<a>标签添加class="selected"属性
    }

    $('#slider .navigation').find('a').click(selectNav);   //当点击navigation类下的<a>标签时，执行selectNav函数




    // go find the navigation link that has this target and select the nav
    function trigger(data) {
        var el = $('#slider .navigation').find('a[href$="' + data.id + '"]').get(0);  //jQuery DOM 元素方法 - get() 方法，可获得该元素的名称和值  见http://www.w3school.com.cn/jquery/dom_element_methods_get.asp
        selectNav.call(el);   //大概相当于，执行selectNav函数，但是其当前指针this为el这个对象  call函数是就来纠正this指针的
    }

    if (window.location.hash) {                            //关于window.location.hash，参见http://www.jsann.com/post/JS_GET_parameters_to_obtain.html
        trigger({ id : window.location.hash.substr(1) });  //substr 方法用于返回一个从指定位置开始的指定长度的子字符串  stringObject.substr(start [, length ])
    } else {
        $('ul.navigation a:first').click();               //如果hash为空，则默认点击的是ul列表中第一个<a>标签，即本项目中的herf＝"#home"
    }



    // offset用于移动到正确的位置，因为我在这里是用了padding，所以我需要从偏移量offset中剪掉padding的部分。这样能得到更佳的效果
    // offset is used to move to *exactly* the right place, since I'm using
    // padding on my example, I need to subtract the amount of padding to
    // the offset.  Try removing this to get a good idea of the effect
    var offset = parseInt((horizontal ? 
        $container.css('paddingTop') : 
        $container.css('paddingLeft')) 
        || 0) * -1;

  
  
  
    // scrollOptions变量定义了serialScroll()和localScroll()函数所需要的参数
    var scrollOptions = {
        target: $scroll, // the element that has the overflow   目标，即所需要滑动显示的部分，以显示出overflow的那部分内容

        // can be a selector which will be relative to the target   一个与目标有联系的选择器
        items: $panels,

        navigation: '.navigation a',

        // selectors are NOT relative to document, i.e. make sure they're unique
        prev: 'img.left', 
        next: 'img.right',

        // allow the scroll effect to run both directions
        axis: 'xy',

        onAfter: trigger, // our final callback     滑动后执行的callback函数

        offset: offset,

        // duration of the sliding effect    滑动所需要的时间
        duration: 500,

        // easing - can be used with the easing plugin: 
        // http://gsgd.co.uk/sandbox/jquery/easing/
        easing: 'swing'
    };

    // apply serialScroll to the slider - we chose this plugin because it 
    // supports// the indexed next and previous scroll along with hooking 
    // in to our navigation.
    $('#slider').serialScroll(scrollOptions);

    // now apply localScroll to hook any other arbitrary links to trigger 
    // the effect
    $.localScroll(scrollOptions);

    // finally, if the URL has a hash, move the slider in to position, 
    // setting the duration to 1 because I don't want it to scroll in the
    // very first page load.  We don't always need this, but it ensures
    // the positioning is absolutely spot on when the pages loads.
    scrollOptions.duration = 1;
    $.localScroll.hash(scrollOptions);

});
