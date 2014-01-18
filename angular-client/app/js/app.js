'use strict';

// Declare app level module which depends on filters, and services
angular.module('TodoApp', [
  'ngRoute',
  'TodoApp.filters',
  'TodoApp.services',
  'TodoApp.directives',
  'TodoApp.controllers'
]).
config(['$routeProvider', function($routeProvider) {
  $routeProvider.when('/list', {
    templateUrl: 'views/list.html', 
    controller: 'ListCtrl'});
  $routeProvider.when('/edit/:id', {
    templateUrl: 'views/detail.html', 
    controller: 'DetailCtrl'});
  $routeProvider.otherwise({redirectTo: '/list'});
}]);
