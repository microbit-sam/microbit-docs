/* Search */

function getSearchTerm()
{
    var sPageURL = window.location.search.substring(1);
    var sURLVariables = sPageURL.split('&');
    for (var i = 0; i < sURLVariables.length; i++)
    {
        var sParameterName = sURLVariables[i].split('=');
        if (sParameterName[0] == 'q') {
            return sParameterName[1];
        }
    }
}

$(document).ready(function() {
    console.log(base_url+"/js/jquery-1.10.2.min.js")
    require([base_url+"/js/jquery-1.10.2.min.js", "https://m.pxt.io/--embed"],renderSnippets);

    var search_term = getSearchTerm(),
        $search_modal = $('#mkdocs_search_modal');

    if(search_term) {
        $search_modal.modal();
    }

    $search_modal.on('shown.bs.modal', function () {
        $search_modal.find('#mkdocs-search-query').focus();
    });

    $('iframe[src*="vimeo.com"]').wrap('<div class="embed-container" />');
    $('iframe[src*="youtube.com"]').wrap('<div class="embed-container" />');
});


function renderSnippets() {
    var path = window.location.href.split('/').pop().split(/[?#]/)[0];
    console.log(path)
    ksRunnerReady(function() {
        pxt.runner.renderAsync({
            snippetClass: 'lang-blocks',
            signatureClass: 'lang-sig',
            blocksClass:'lang-block',
            shuffleClass: 'lang-shuffle',
            simulatorClass: 'lang-sim',
            linksClass: 'lang-cards',
            namespacesClass: 'lang-namespaces',
            codeCardClass: 'lang-codecard',
            snippetReplaceParent: true,
            simulator: true,
            hex: true,
            hexName: path
        }).done();
    });
}

/* Highlight */
$( document ).ready(function() {

    hljs.configure({ languages: ["cpp"] });
    hljs.initHighlightingOnLoad();

    $('table').addClass('table table-striped table-hover');

    if(window.location.pathname.indexOf("online-toolchains") > 0){
        $(".table th:nth-child(1)").css("width",'25%');
        $(".table").css("table-layout","fixed");
        $(".table th:nth-child(2)").css("width",'75%');
    }
});


$('body').scrollspy({
    target: '.bs-sidebar',
});

/* Toggle the `clicky` class on the body when clicking links to let us
   retrigger CSS animations. See ../css/base.css for more details. */
$('a').click(function(e) {
    $('body').toggleClass('clicky');
});

/* Prevent disabled links from causing a page reload */
$("li.disabled a").click(function() {
    event.preventDefault();
});
