'use strict';

/* Services */

angular.module('myApp.services', ['ngResource'])
    .value('apiUrl', 'http://localhost:8000/api/')
    .factory('Tasks', ['$resource', function($resource) {
        return $resource('http://localhost:8000/api/tasks/:id.json', {id: '@id'}, 
            { 'get':    {method:'GET'},
              'save':   {method:'POST'},
              'update': {method:'PUT'},
              'query':  {method:'GET', isArray:true},
              'remove': {method:'DELETE'},
              'delete': {method:'DELETE'} }
              );
    }])
    .value('version', '0.1');
