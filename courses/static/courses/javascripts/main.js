var app = angular.module('coursesApp', ['ngResource', 'ngRoute', 'ngSanitize', 'ngAnimate', 'monospaced.elastic', 'angularFileUpload']);

app.config(function($routeProvider, $resourceProvider){
	var basePath = '/static/courses/html/';
	$routeProvider.when('/', {
			templateUrl: basePath + 'index.html',
			controller: 'HomeController'
		})
		.when('/about', {
			templateUrl: basePath + 'about.html',
			controller: 'AboutController'
		})
		.when('/new', {
			templateUrl: basePath + 'new.html',
			controller: 'NewCourseController'
		})
    .when('/:courseId/view/:pageId', {
      templateUrl: basePath + 'show.html',
      controller: 'ViewCourseController'
    })
		.when('/:courseId/edit/:pageId', {
			templateUrl: basePath + 'edit.html',
			controller: 'EditCourseController'
		})
    .when('/:courseId/preview/:pageId', {
      templateUrl: basePath + 'preview.html',
      controller: 'PreviewCourseController'
    })
		.otherwise({
			templateUrl: basePath + '404.html'
		});
    $resourceProvider.defaults.stripTrailingSlashes = true;
});

app.factory('Course', ['$resource', function($resource) {
  return $resource(
      'api/courses/:courseId',
      {courseId: '@id'}
    );
}]);

app.filter('markdown', function() {
  return function(input) {
    var converter = new Showdown.converter({ extensions: ['courses'] });
    return converter.makeHtml(input);
  };
});

app.filter('trust', function($sce){
  return function(input) {
    return $sce.trustAsHtml(input);
  };
});

app.directive('mathjax', ['$timeout', function($timeout) {
  return {
    restrict: 'AE',
    link: function(scope, element, attrs) {
      $timeout(function () {
        MathJax.Hub.Queue(["Typeset", MathJax.Hub, element[0]]);
        MathJax.Hub.Queue(function() {
          element.removeClass("ng-hide");
        })
      });
    }
  };
}]);

app.controller('HomeController', ['$scope', '$location', 'Course', function($scope, $location, Course) {
	$scope.courses = Course.query();

	$scope.showCourse = function(course) {
		$location.path(course.id + "/view/1");
	};

}]);

app.controller('AboutController', function() {
	
});

app.controller('NewCourseController', function($scope, $location) {
	$scope.create = function() {
		// TODO: save data to the server
		$location.path("1/edit/1");
	};
});

app.controller('EditCourseController', ['$scope', '$routeParams', '$location','Course', '$upload', function($scope, $routeParams, $location, Course, $upload) {
	// TODO: fetch only the right page
  $scope.course = Course.get({courseId: $routeParams.courseId }, function(course) {
    $scope.page = course.pages[$routeParams.pageId];
  });

  $scope.newSection = function() {
    // TODO: add in the database
    $scope.page.sections["6"] = {"content":""}
  };
  $scope.removeSection = function(id) {
    // TODO: delete in the database
    delete $scope.page.sections[id]
  };
  $scope.saveCourse = function() {
    // TODO: save course in the databse 
  };
  $scope.newPage = function() {
    // TODO: save course in the database and add a new page
    $location.path($scope.course.id + "/edit/2")
  };
  $scope.isCurrentPage = function(page) {
    return page.id === $scope.page.id;
  };
  $scope.onFileSelect = function($files) {
    for (var i = 0; i < $files.length; i++) {
      var file = $files[i];
      $scope.upload = $upload.upload({
        url: '/upload',
        method: 'POST',
        file: file
      }).progress(function(evt) {
        console.log('percent: ' + parseInt(100.0 * evt.loaded / evt.total));
      }).success(function(data, status, headers, config) {
        console.log("success");
      }).error(function() {
        console.log("error");
      });
    }
  };
}]);

app.controller('PreviewCourseController', ['$scope', '$routeParams', 'Course', function($scope, $routeParams, Course) {
  // TODO: fetch only the right page
  $scope.course = Course.get({courseId: $routeParams.courseId }, function(course) {
    $scope.page = course.pages[$routeParams.pageId];
  });
}]);

app.controller('ViewCourseController', ['$scope', '$routeParams', '$location', 'Course', function($scope, $routeParams, $location, Course) {
  $scope.course = Course.get({courseId: $routeParams.courseId }, function(course) {
    $scope.page = course.pages[$routeParams.pageId];
    $scope.firstPage = function() {
      return $scope.page.id === 1;
    };
    $scope.lastPage = function() {
      return $scope.page.id === Object.keys($scope.course.pages).length;
    };
  });

  $scope.nextPage = function() {
    $location.path($scope.course.id + "/view/" + ($scope.page.id + 1));
  };
  $scope.previousPage = function() {
    $location.path($scope.course.id + "/view/" + ($scope.page.id - 1));
  };
}]);
