/**
* Posts
* @namespace app.blog.services
*/
(function () {
  'use strict';

  angular
    .module('app.blog.services')
    .factory('Blog', Blog);

  Blog.$inject = ['$http'];

  /**
  * @namespace Blog
  * @returns {Factory}
  */
  function Blog($http) {
    var Blog = {
      all: all,
      create: create,
      get: get
    };

    return Blog;

    ////////////////////

    /**
    * @name all
    * @desc Get all Blog
    * @returns {Promise}
    * @memberOf app.posts.services.Posts
    */
    function all() {
      return $http.get('/api/v1/blog/');
    }


    /**
    * @name create
    * @desc Create a new Post
    * @param {string} content The content of the new Post
    * @returns {Promise}
    * @memberOf app.posts.services.Posts
    */
    function create(title, content) {
      return $http.post('/api/v1/blog/', {
        title: title,
        content: content
      });
    }

    /**
     * @name get
     * @desc Get the Posts of a given user
     * @param {string} username The username to get Posts for
     * @returns {Promise}
     * @memberOf app.posts.services.Posts
     */
    function get(username) {
      return $http.get('/api/v1/blog/');
    }
  }
})();
