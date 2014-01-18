'use strict';

/* Services */

angular.module('TodoApp.services', ['ngResource'])
    .factory('Tasks', ['$resource', function($resource) {
        //return $resource('http://localhost:8000/api/tasks/:id', {id: '@id'}, 
        return $resource('http://todo-rest.herokuapp.com/api/tasks/:id', {id: '@id'}, 
            { 'get':    {method:'GET'},
              'save':   {method:'POST'},
              'update': {method:'PUT'},
              'query':  {method:'GET', isArray:true},
              'remove': {method:'DELETE'},
              'delete': {method:'DELETE'} }
              );
    }])
    .value('version', '0.1');
