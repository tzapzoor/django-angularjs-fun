/**
* PostsController
* @namespace app.posts.controllers
*/
(function () {
  'use strict';

  angular
    .module('app.blog.controllers')
    .controller('BlogController', BlogController);

  BlogController.$inject = ['$scope', 'Blog', 'Authentication'];

  /**
  * @namespace PostsController
  */
  function BlogController($scope, Blog, Authentication) {
    var vm = this;

    activate();

    /**
    * @name activate
    * @desc Actions to be performed when this controller is instantiated
    * @memberOf app.posts.controllers.PostsController
    */
    function activate() {
        Blog.all().then(blogSuccessCallback, null);

        function blogSuccessCallback(data, status) {
          vm.blog = data.data;
        }
    }

    $scope.createBlogPost = function(title, content) {
      var current_username = Authentication.getAuthenticatedAccount().username;
      var current_unix_time = getCurrentUnixTime();
      Blog.create(title, content);
      vm.blog.unshift( {'title': title, 'content': content, 'author': {'username': current_username}, 'created_at': current_unix_time, 'updated_at': current_unix_time} )
    }

  }
})();


function getCurrentUnixTime() {
    var d = new Date();
    return current_time = Math.ceil(d.getTime()/1000);
}
