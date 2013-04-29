var ArticleFilter = {
    init: function() {
        $('.type-filter').on('click', $.proxy(function(event){
            var filterElement = $(event.target).parent('.type-filter');
            var listContainer = $('#article-list');
            if(filterElement.hasClass('active')){
                listContainer.data('filter-args-filter', null);
            } else {
                listContainer.data('filter-args-filter', filterElement.data('filter'));
            }
            listContainer.data('filter-args-page', 1);
            this.collectArgsAndSumbit();
        }, this));

        $('[data-page]').on('click', $.proxy(function(event){
            event.preventDefault();
            var paginationElement = $(event.target).closest('li');

            $('#article-list').data('filter-args-page', paginationElement.data('page'));

            this.collectArgsAndSumbit();
        }, this));
    },

    updateHistory: function(args){
        this.historyFlag = false;
        History.pushState(args, null, "?" + $.param(args));
    },

    collectArgsAndSumbit: function(){
        var nonRequiredArgs = this.collectNonRequiredArgs();
        this.submit(nonRequiredArgs);
    },

    collectNonRequiredArgs: function(){
        var filterArgsPrefix = "filterArgs";
        return this.collectArgs(filterArgsPrefix);
    },

    collectRequiredArgs: function(){
        var filterArgsPrefix = "filterRequiredArgs";
        return this.collectArgs(filterArgsPrefix);
    },

    collectArgs: function(argsPrefix){
        var args = {};

        $.each($('#article-list').data(), function(key,value){
            if(value != null && key.substring(0, argsPrefix.length) === argsPrefix){
                var arg = key.replace(argsPrefix,'').toLowerCase();
                args[arg] = value;
            }
        });

        return args;
    },

    historyBind: function(){
        History.Adapter.bind(window,'statechange',$.proxy(function(){
            if(this.historyFlag){
                var State = History.getState();
                var filterEndpoint = $('#article-list').data('filter-endpoint');
                this.submit(State.data)
            }
            this.historyFlag = true;
        }, this));
    },

    submit: function(nonRequiredArgs){
        this.updateHistory(nonRequiredArgs);
        var requiredArgs = this.collectRequiredArgs();
        var args = $.extend({}, nonRequiredArgs, requiredArgs);
        var filterEndpoint = $('#article-list').data('filter-endpoint');
        Dajaxice.pari.article[filterEndpoint](Dajax.process, args);
    },

    historyFlag: true
}

$(function(){
    ArticleFilter.init();
    ArticleFilter.historyBind();
    $('.type-filter').tooltip();
});