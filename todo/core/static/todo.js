var app = angular.module('project', ['ngRoute', 'ngResource']);

app.factory('Tasks', ['$resource', function($resource) {
  return $resource("/api/tasks/", {});
}]);

app.controller('TodoCtrl', ['$scope', 'Tasks', function($scope, Tasks) {
  $scope.todos = Tasks.query();

  //[
  //  {title:'aprender angular', done:true},
  //  {title:'construir um app angular', done:false}
  //];

  $scope.addTodo = function() {
    $scope.todos.push({title:$scope.todoText, done:false});
    $scope.todoText = '';
  };

  $scope.remaining = function() {
    var count = 0;
    angular.forEach($scope.todos, function(todo) {
      count += todo.done ? 0 : 1;
    });
    return count;
  };

  $scope.archive = function() {
    var oldTodos = $scope.todos;
    $scope.todos = [];
    angular.forEach(oldTodos, function(todo) {
      if (!todo.done) $scope.todos.push(todo);
    });
  };
}]);
