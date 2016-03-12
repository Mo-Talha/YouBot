angular.module('core.routes', [])
    .config(['$stateProvider', '$urlRouterProvider', "$locationProvider",
        function($stateProvider, $urlRouterProvider, $locationProvider) {

        $urlRouterProvider.otherwise("/");
        $locationProvider.html5Mode(true);

        $stateProvider
            .state('app', {
                url: '/',
                templateUrl:'/dashboard',
                controller: 'coreController'
            });

    }]);