'use strict';

/* Controllers */

angular.module('myApp.controllers', []).
  controller('ListCtrl', ['$scope', '$location', 'Tasks', 
    function($scope, $location, Tasks) {
    $scope.data = Tasks.query();
    $scope.taskTitle = '';

    $scope.addTask = function() {
      Tasks.save({title: $scope.taskTitle}, function(data) {
        $scope.data.push(data);
        $scope.taskTitle = '';
      });
    };

    $scope.updateDone = function(task) {
      task.$update();
    };

    $scope.removeTodo = function(task) {
      task.$remove();
      $scope.data.splice($scope.data.indexOf(task), 1);
    };

    $scope.editTask = function(task) {
      $location.path("/edit/" + task.id.toString());
    }
  }])
  .controller('DetailCtrl', ['$scope', '$routeParams', '$location', 'Tasks', 
    function($scope, $routeParams, $location, Tasks) {
    $scope.task = Tasks.get({id: $routeParams.id});
    $scope.updateTask = function() {
      $scope.task.$update();
      $location.path("/list");
    };
    $scope.cancelEdit = function() {
      $location.path("/list");
    };
    $scope.removeTask = function() {
      $scope.task.$remove();
      $location.path("/list");
    };
  }]);

