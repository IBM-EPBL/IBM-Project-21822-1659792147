"use strict";
/*
 * ATTENTION: An "eval-source-map" devtool has been used.
 * This devtool is neither made for production nor for readable output files.
 * It uses "eval()" calls to create a separate source file with attached SourceMaps in the browser devtools.
 * If you are trying to read the output file, select a different devtool (https://webpack.js.org/configuration/devtool/)
 * or disable the default devtool with "devtool: false".
 * If you are looking for production-ready output files, see mode: "production" (https://webpack.js.org/configuration/mode/).
 */
(() => {
var exports = {};
exports.id = "pages/api/auth/[...nextauth]";
exports.ids = ["pages/api/auth/[...nextauth]"];
exports.modules = {

/***/ "next-auth":
/*!****************************!*\
  !*** external "next-auth" ***!
  \****************************/
/***/ ((module) => {

module.exports = require("next-auth");

/***/ }),

/***/ "next-auth/providers/google":
/*!*********************************************!*\
  !*** external "next-auth/providers/google" ***!
  \*********************************************/
/***/ ((module) => {

module.exports = require("next-auth/providers/google");

/***/ }),

/***/ "(api)/./pages/api/auth/[...nextauth].js":
/*!*****************************************!*\
  !*** ./pages/api/auth/[...nextauth].js ***!
  \*****************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

eval("__webpack_require__.r(__webpack_exports__);\n/* harmony export */ __webpack_require__.d(__webpack_exports__, {\n/* harmony export */   \"authOptions\": () => (/* binding */ authOptions),\n/* harmony export */   \"default\": () => (__WEBPACK_DEFAULT_EXPORT__)\n/* harmony export */ });\n/* harmony import */ var next_auth__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! next-auth */ \"next-auth\");\n/* harmony import */ var next_auth__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(next_auth__WEBPACK_IMPORTED_MODULE_0__);\n/* harmony import */ var next_auth_providers_google__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! next-auth/providers/google */ \"next-auth/providers/google\");\n/* harmony import */ var next_auth_providers_google__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(next_auth_providers_google__WEBPACK_IMPORTED_MODULE_1__);\n\n\nconst createUser = async (name = \"\", email)=>{\n    if (!email) return false;\n    try {\n        await fetch(`${process.env.REWRITE_SERVER_URL}/createuser`, {\n            method: \"POST\",\n            headers: {\n                \"Content-Type\": \"application/json\"\n            },\n            body: JSON.stringify({\n                name,\n                email\n            })\n        });\n        return true;\n    } catch (err) {\n        console.log(err);\n    }\n    return false;\n};\nconst authOptions = {\n    providers: [\n        next_auth_providers_google__WEBPACK_IMPORTED_MODULE_1___default()({\n            clientId: process.env.GOOGLE_ID,\n            clientSecret: process.env.GOOGLE_SECRET\n        })\n    ],\n    callbacks: {\n        async signIn ({ user  }) {\n            await createUser(user.name, user.email);\n            return true;\n        }\n    }\n};\n/* harmony default export */ const __WEBPACK_DEFAULT_EXPORT__ = (next_auth__WEBPACK_IMPORTED_MODULE_0___default()(authOptions));\n//# sourceURL=[module]\n//# sourceMappingURL=data:application/json;charset=utf-8;base64,eyJ2ZXJzaW9uIjozLCJmaWxlIjoiKGFwaSkvLi9wYWdlcy9hcGkvYXV0aC9bLi4ubmV4dGF1dGhdLmpzLmpzIiwibWFwcGluZ3MiOiI7Ozs7Ozs7OztBQUFpQztBQUN1QjtBQUV4RCxNQUFNRSxhQUFhLE9BQU9DLE9BQU8sRUFBRSxFQUFFQyxRQUFVO0lBQzdDLElBQUksQ0FBQ0EsT0FBTyxPQUFPLEtBQUs7SUFFeEIsSUFBSTtRQUNGLE1BQU1DLE1BQU0sQ0FBQyxFQUFFQyxRQUFRQyxHQUFHLENBQUNDLGtCQUFrQixDQUFDLFdBQVcsQ0FBQyxFQUFFO1lBQzFEQyxRQUFRO1lBQ1JDLFNBQVM7Z0JBQ1AsZ0JBQWdCO1lBQ2xCO1lBQ0FDLE1BQU1DLEtBQUtDLFNBQVMsQ0FBQztnQkFBRVY7Z0JBQU1DO1lBQU07UUFDckM7UUFDQSxPQUFPLElBQUk7SUFDYixFQUFFLE9BQU9VLEtBQUs7UUFDWkMsUUFBUUMsR0FBRyxDQUFDRjtJQUNkO0lBQ0EsT0FBTyxLQUFLO0FBQ2Q7QUFFTyxNQUFNRyxjQUFjO0lBQ3pCQyxXQUFXO1FBQ1RqQixpRUFBY0EsQ0FBQztZQUNia0IsVUFBVWIsUUFBUUMsR0FBRyxDQUFDYSxTQUFTO1lBQy9CQyxjQUFjZixRQUFRQyxHQUFHLENBQUNlLGFBQWE7UUFDekM7S0FDRDtJQUNEQyxXQUFXO1FBQ1QsTUFBTUMsUUFBTyxFQUFFQyxLQUFJLEVBQUUsRUFBRTtZQUNyQixNQUFNdkIsV0FBV3VCLEtBQUt0QixJQUFJLEVBQUVzQixLQUFLckIsS0FBSztZQUN0QyxPQUFPLElBQUk7UUFDYjtJQUNGO0FBQ0YsRUFBRTtBQUVGLGlFQUFlSixnREFBUUEsQ0FBQ2lCLFlBQVlBLEVBQUMiLCJzb3VyY2VzIjpbIndlYnBhY2s6Ly9uZXdzLWFwcC8uL3BhZ2VzL2FwaS9hdXRoL1suLi5uZXh0YXV0aF0uanM/NTI3ZiJdLCJzb3VyY2VzQ29udGVudCI6WyJpbXBvcnQgTmV4dEF1dGggZnJvbSBcIm5leHQtYXV0aFwiO1xuaW1wb3J0IEdvb2dsZVByb3ZpZGVyIGZyb20gXCJuZXh0LWF1dGgvcHJvdmlkZXJzL2dvb2dsZVwiO1xuXG5jb25zdCBjcmVhdGVVc2VyID0gYXN5bmMgKG5hbWUgPSBcIlwiLCBlbWFpbCkgPT4ge1xuICBpZiAoIWVtYWlsKSByZXR1cm4gZmFsc2U7XG5cbiAgdHJ5IHtcbiAgICBhd2FpdCBmZXRjaChgJHtwcm9jZXNzLmVudi5SRVdSSVRFX1NFUlZFUl9VUkx9L2NyZWF0ZXVzZXJgLCB7XG4gICAgICBtZXRob2Q6IFwiUE9TVFwiLFxuICAgICAgaGVhZGVyczoge1xuICAgICAgICBcIkNvbnRlbnQtVHlwZVwiOiBcImFwcGxpY2F0aW9uL2pzb25cIixcbiAgICAgIH0sXG4gICAgICBib2R5OiBKU09OLnN0cmluZ2lmeSh7IG5hbWUsIGVtYWlsIH0pLFxuICAgIH0pO1xuICAgIHJldHVybiB0cnVlO1xuICB9IGNhdGNoIChlcnIpIHtcbiAgICBjb25zb2xlLmxvZyhlcnIpO1xuICB9XG4gIHJldHVybiBmYWxzZTtcbn07XG5cbmV4cG9ydCBjb25zdCBhdXRoT3B0aW9ucyA9IHtcbiAgcHJvdmlkZXJzOiBbXG4gICAgR29vZ2xlUHJvdmlkZXIoe1xuICAgICAgY2xpZW50SWQ6IHByb2Nlc3MuZW52LkdPT0dMRV9JRCxcbiAgICAgIGNsaWVudFNlY3JldDogcHJvY2Vzcy5lbnYuR09PR0xFX1NFQ1JFVCxcbiAgICB9KSxcbiAgXSxcbiAgY2FsbGJhY2tzOiB7XG4gICAgYXN5bmMgc2lnbkluKHsgdXNlciB9KSB7XG4gICAgICBhd2FpdCBjcmVhdGVVc2VyKHVzZXIubmFtZSwgdXNlci5lbWFpbCk7XG4gICAgICByZXR1cm4gdHJ1ZTtcbiAgICB9LFxuICB9LFxufTtcblxuZXhwb3J0IGRlZmF1bHQgTmV4dEF1dGgoYXV0aE9wdGlvbnMpO1xuIl0sIm5hbWVzIjpbIk5leHRBdXRoIiwiR29vZ2xlUHJvdmlkZXIiLCJjcmVhdGVVc2VyIiwibmFtZSIsImVtYWlsIiwiZmV0Y2giLCJwcm9jZXNzIiwiZW52IiwiUkVXUklURV9TRVJWRVJfVVJMIiwibWV0aG9kIiwiaGVhZGVycyIsImJvZHkiLCJKU09OIiwic3RyaW5naWZ5IiwiZXJyIiwiY29uc29sZSIsImxvZyIsImF1dGhPcHRpb25zIiwicHJvdmlkZXJzIiwiY2xpZW50SWQiLCJHT09HTEVfSUQiLCJjbGllbnRTZWNyZXQiLCJHT09HTEVfU0VDUkVUIiwiY2FsbGJhY2tzIiwic2lnbkluIiwidXNlciJdLCJzb3VyY2VSb290IjoiIn0=\n//# sourceURL=webpack-internal:///(api)/./pages/api/auth/[...nextauth].js\n");

/***/ })

};
;

// load runtime
var __webpack_require__ = require("../../../webpack-api-runtime.js");
__webpack_require__.C(exports);
var __webpack_exec__ = (moduleId) => (__webpack_require__(__webpack_require__.s = moduleId))
var __webpack_exports__ = (__webpack_exec__("(api)/./pages/api/auth/[...nextauth].js"));
module.exports = __webpack_exports__;

})();