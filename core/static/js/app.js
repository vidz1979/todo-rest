'use strict';

// Declare app level module which depends on filters, and services
angular.module('myApp', [
  'ngRoute',
  'myApp.filters',
  'myApp.services',
  'myApp.directives',
  'myApp.controllers'
]).
config(['$routeProvider', function($routeProvider) {
  $routeProvider.when('/list', {
    templateUrl: 'https://todo-rest.s3.amazonaws.com/partials/list.html', 
    controller: 'ListCtrl'});
  $routeProvider.when('/edit/:id', {
    templateUrl: 'https://todo-rest.s3.amazonaws.com/partials/detail.html', 
    controller: 'DetailCtrl'});
  $routeProvider.otherwise({redirectTo: '/list'});
}]);
