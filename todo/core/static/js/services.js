'use strict';

/* Services */

angular.module('myApp.services', ['ngResource'])
    .factory('Tasks', ['$resource', function($resource) {
        return $resource('/api/tasks/:id', {id: '@id'}, 
            { 'get':    {method:'GET'},
              'save':   {method:'POST'},
              'update': {method:'PUT'},
              'query':  {method:'GET', isArray:true},
              'remove': {method:'DELETE'},
              'delete': {method:'DELETE'} }
              );
    }])
    .value('version', '0.1');
