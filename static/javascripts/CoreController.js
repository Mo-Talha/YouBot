angular.module('core.controller', [])
    .controller('coreController', ['$scope', 'Upload', '$timeout', 'coreServices',
        function ($scope, Upload, $timeout, coreServices) {

            $scope.uploadFiles = function(files) {
                $scope.files = files;
                angular.forEach(files, function(file) {
                    file.upload = Upload.upload({
                        url: '/process_image',
                        data: {file: file}
                    });

                    file.upload.then(function (response) {
                        $timeout(function () {
                            file.result = response.data;
                        });
                    }, function (response) {
                        if (response.status > 0)
                            $scope.errorMsg = response.status + ': ' + response.data;
                    });
                });
            }

    }]);