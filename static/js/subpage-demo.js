$(document).ready(function () {
    $(document).on('click', '.demo .settings', function (e) {
        e.preventDefault();
        if ($(this).parent().attr('style') === 'left: 0px;') {
            $(this).parent().animate({ 'left': '-200px' });
        }
        else {
            $(this).parent().animate({ 'left': '0' });
        }
    });

    if ($.cookie('color')) {
        $('#color').attr('href', '../css/colors/' + $.cookie('color'));
    }
    $(document).on('click', '.demo .color',function (e) {
        e.preventDefault();
        $.cookie('color', $(this).data('color'), { expires: 7, path: '/' });
        $('#color').attr('href', '../css/colors/' + $(this).data('color'));
    });

    if ($.cookie('box')) {
        $('html').addClass($.cookie('box'));
    }
    $(document).on('click', '.demo .boxed', function (e) {
        e.preventDefault();
        $.cookie('box', $(this).data('box'), { expires: 7, path: '/' });
        $('html').removeAttr('class').addClass($(this).data('box'));
        window.location.href = 'index.html';
    });

    if ($.cookie('background')) {
        if ($.cookie('box')) {
            $('body').css({ 'background-image': 'url(Theme/img/bg/' + $.cookie('background') + ')' });
        }
    }
    $(document).on('click', '.demo .background', function (e) {
        e.preventDefault();
        if ($.cookie('box')) {
            $.cookie('background', $(this).data('background'), { expires: 7, path: '/' });
            $('body').css({ 'background-image': 'url(Theme/img/bg/' + $(this).data('background') + ')' });
        }
    });

    $(document).on('click', '.demo .reset', function (e) {
        e.preventDefault();
        $('#color').attr('href', '../css/colors/yellow.css');
        $('html').removeClass('boxed');
        $('body').removeAttr('style');
        $.removeCookie('color', { path: '/' });
        $.removeCookie('box', { path: '/' });
        $.removeCookie('background', { path: '/' });
    });

    var html = '' +
        '<div class="demo">' +
        '<a href="#" class="settings">' +
        '<i class="fa fa-cog fa-spin"></i>' +
        '</a>' +
        '<h5>SELECT A COLOR</h5>' +
        '<a href="#" class="color" data-color="yellow.css" style="background-color:#ffb100"></a>' +
        '<a href="#" class="color" data-color="green2.css" style="background-color:#52bf00"></a>' +
        '<a href="#" class="color" data-color="red.css" style="background-color:#d81300"></a>' +
        '<a href="#" class="color" data-color="blue.css" style="background-color:#425cbb"></a>' +
        '<a href="#" class="color" data-color="Purple.css" style="background-color:#BF55EC"></a>' +
        '<a href="#" class="color" data-color="turquoise.css" style="background-color:#00b4d9"></a>' +
        '<a href="#" class="color" data-color="green.css" style="background-color:#029A83"></a>' +
        '<a href="#" class="color" data-color="pink.css" style="background-color:#ef3e96"></a>' +
        '<a href="#" class="color" data-color="orange.css" style="background-color:#ff5a14"></a>' +
        '<a href="#" class="color" data-color="grey.css" style="background-color:#ABB7B7"></a>' +
        '<hr />' +
        '<a href="#" class="reset btn btn-sm btn-info p-l-30 p-r-30">Reset</a>' +
        '</div>';
    $('body').append(html);
});