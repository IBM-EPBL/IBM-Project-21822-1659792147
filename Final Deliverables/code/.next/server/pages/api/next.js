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
exports.id = "pages/api/next";
exports.ids = ["pages/api/next"];
exports.modules = {

/***/ "(api)/./lib/origins.js":
/*!************************!*\
  !*** ./lib/origins.js ***!
  \************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

eval("__webpack_require__.r(__webpack_exports__);\n/* harmony export */ __webpack_require__.d(__webpack_exports__, {\n/* harmony export */   \"ALLOWED_ORIGINS\": () => (/* binding */ ALLOWED_ORIGINS)\n/* harmony export */ });\nconst ALLOWED_ORIGINS = [\n    \"http://localhost:3000\",\n    \"https://fingertip-news.vercel.app\",\n    \"https://theprint.me\",\n    \"https://www.theprint.me\"\n];\n//# sourceURL=[module]\n//# sourceMappingURL=data:application/json;charset=utf-8;base64,eyJ2ZXJzaW9uIjozLCJmaWxlIjoiKGFwaSkvLi9saWIvb3JpZ2lucy5qcy5qcyIsIm1hcHBpbmdzIjoiOzs7O0FBQU8sTUFBTUEsa0JBQWtCO0lBQzNCO0lBQ0E7SUFDQTtJQUNBO0NBQ0gsQ0FBQyIsInNvdXJjZXMiOlsid2VicGFjazovL25ld3MtYXBwLy4vbGliL29yaWdpbnMuanM/YmFjMCJdLCJzb3VyY2VzQ29udGVudCI6WyJleHBvcnQgY29uc3QgQUxMT1dFRF9PUklHSU5TID0gW1xuICAgIFwiaHR0cDovL2xvY2FsaG9zdDozMDAwXCIsXG4gICAgXCJodHRwczovL2ZpbmdlcnRpcC1uZXdzLnZlcmNlbC5hcHBcIixcbiAgICBcImh0dHBzOi8vdGhlcHJpbnQubWVcIixcbiAgICBcImh0dHBzOi8vd3d3LnRoZXByaW50Lm1lXCIsXG5dO1xuIl0sIm5hbWVzIjpbIkFMTE9XRURfT1JJR0lOUyJdLCJzb3VyY2VSb290IjoiIn0=\n//# sourceURL=webpack-internal:///(api)/./lib/origins.js\n");

/***/ }),

/***/ "(api)/./pages/api/next.ts":
/*!***************************!*\
  !*** ./pages/api/next.ts ***!
  \***************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

eval("__webpack_require__.r(__webpack_exports__);\n/* harmony export */ __webpack_require__.d(__webpack_exports__, {\n/* harmony export */   \"default\": () => (/* binding */ handler)\n/* harmony export */ });\n/* harmony import */ var _lib_origins__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! ../../lib/origins */ \"(api)/./lib/origins.js\");\n\nasync function handler(req, res) {\n    try {\n        const { url , nextIndex , activeTopic  } = req.body;\n        const { origin  } = req.headers;\n        if (origin && _lib_origins__WEBPACK_IMPORTED_MODULE_0__.ALLOWED_ORIGINS.indexOf(origin) === -1) {\n            return res.status(403).json({\n                data: [],\n                error: \"Forbidden\",\n                next: null\n            });\n        }\n        res.setHeader(\"Access-Control-Allow-Origin\", origin || \"*\");\n        if (typeof url !== \"string\") return res.status(400).json({\n            error: \"Invalid url\",\n            data: [],\n            next: null\n        });\n        const parsedURL = `${process.env.API_URL}?url=${encodeURIComponent(url)}&nextIndex=${nextIndex}&activeTopic=${activeTopic}&activeNavIndex=0&topicEngName=${activeTopic}`;\n        const response = await fetch(parsedURL);\n        const json = await response.json();\n        res.status(200).json({\n            data: json?.data?.rows || [],\n            next: json?.url || null,\n            nextIndex: json?.nextIndex || null,\n            activeTopic: json?.activeTopic || null\n        });\n    } catch (err) {\n        console.log(err);\n        res.status(500);\n    }\n}\n//# sourceURL=[module]\n//# sourceMappingURL=data:application/json;charset=utf-8;base64,eyJ2ZXJzaW9uIjozLCJmaWxlIjoiKGFwaSkvLi9wYWdlcy9hcGkvbmV4dC50cy5qcyIsIm1hcHBpbmdzIjoiOzs7OztBQUNvRDtBQVVyQyxlQUFlQyxRQUM1QkMsR0FBbUIsRUFDbkJDLEdBQTBCLEVBQzFCO0lBQ0EsSUFBSTtRQUNGLE1BQU0sRUFBRUMsSUFBRyxFQUFFQyxVQUFTLEVBQUVDLFlBQVcsRUFBRSxHQUFHSixJQUFJSyxJQUFJO1FBRWhELE1BQU0sRUFBRUMsT0FBTSxFQUFFLEdBQUdOLElBQUlPLE9BQU87UUFFOUIsSUFBSUQsVUFBVVIsaUVBQXVCLENBQUNRLFlBQVksQ0FBQyxHQUFHO1lBQ3BELE9BQU9MLElBQUlRLE1BQU0sQ0FBQyxLQUFLQyxJQUFJLENBQUM7Z0JBQUVDLE1BQU0sRUFBRTtnQkFBRUMsT0FBTztnQkFBYUMsTUFBTSxJQUFJO1lBQUM7UUFDekUsQ0FBQztRQUVEWixJQUFJYSxTQUFTLENBQUMsK0JBQStCUixVQUFVO1FBRXZELElBQUksT0FBT0osUUFBUSxVQUNqQixPQUFPRCxJQUNKUSxNQUFNLENBQUMsS0FDUEMsSUFBSSxDQUFDO1lBQUVFLE9BQU87WUFBZUQsTUFBTSxFQUFFO1lBQUVFLE1BQU0sSUFBSTtRQUFDO1FBRXZELE1BQU1FLFlBQVksQ0FBQyxFQUFFQyxRQUFRQyxHQUFHLENBQUNDLE9BQU8sQ0FBQyxLQUFLLEVBQUVDLG1CQUM5Q2pCLEtBQ0EsV0FBVyxFQUFFQyxVQUFVLGFBQWEsRUFBRUMsWUFBWSwrQkFBK0IsRUFBRUEsWUFBWSxDQUFDO1FBQ2xHLE1BQU1nQixXQUFXLE1BQU1DLE1BQU1OO1FBQzdCLE1BQU1MLE9BQU8sTUFBTVUsU0FBU1YsSUFBSTtRQUVoQ1QsSUFBSVEsTUFBTSxDQUFDLEtBQUtDLElBQUksQ0FBQztZQUNuQkMsTUFBTUQsTUFBTUMsTUFBTVcsUUFBUSxFQUFFO1lBQzVCVCxNQUFNSCxNQUFNUixPQUFPLElBQUk7WUFDdkJDLFdBQVdPLE1BQU1QLGFBQWEsSUFBSTtZQUNsQ0MsYUFBYU0sTUFBTU4sZUFBZSxJQUFJO1FBQ3hDO0lBQ0YsRUFBRSxPQUFPbUIsS0FBSztRQUNaQyxRQUFRQyxHQUFHLENBQUNGO1FBQ1p0QixJQUFJUSxNQUFNLENBQUM7SUFDYjtBQUNGLENBQUMiLCJzb3VyY2VzIjpbIndlYnBhY2s6Ly9uZXdzLWFwcC8uL3BhZ2VzL2FwaS9uZXh0LnRzP2UwMmUiXSwic291cmNlc0NvbnRlbnQiOlsiaW1wb3J0IHR5cGUgeyBOZXh0QXBpUmVxdWVzdCwgTmV4dEFwaVJlc3BvbnNlIH0gZnJvbSBcIm5leHRcIjtcbmltcG9ydCB7IEFMTE9XRURfT1JJR0lOUyB9IGZyb20gXCIuLi8uLi9saWIvb3JpZ2luc1wiO1xuXG50eXBlIERhdGEgPSB7XG4gIGRhdGE6IFtdO1xuICBuZXh0OiBudWxsIHwgc3RyaW5nO1xuICBlcnJvcj86IHN0cmluZztcbiAgbmV4dEluZGV4Pzogc3RyaW5nO1xuICBhY3RpdmVUb3BpYz86IHN0cmluZztcbn07XG5cbmV4cG9ydCBkZWZhdWx0IGFzeW5jIGZ1bmN0aW9uIGhhbmRsZXIoXG4gIHJlcTogTmV4dEFwaVJlcXVlc3QsXG4gIHJlczogTmV4dEFwaVJlc3BvbnNlPERhdGE+XG4pIHtcbiAgdHJ5IHtcbiAgICBjb25zdCB7IHVybCwgbmV4dEluZGV4LCBhY3RpdmVUb3BpYyB9ID0gcmVxLmJvZHk7XG5cbiAgICBjb25zdCB7IG9yaWdpbiB9ID0gcmVxLmhlYWRlcnM7XG5cbiAgICBpZiAob3JpZ2luICYmIEFMTE9XRURfT1JJR0lOUy5pbmRleE9mKG9yaWdpbikgPT09IC0xKSB7XG4gICAgICByZXR1cm4gcmVzLnN0YXR1cyg0MDMpLmpzb24oeyBkYXRhOiBbXSwgZXJyb3I6IFwiRm9yYmlkZGVuXCIsIG5leHQ6IG51bGwgfSk7XG4gICAgfVxuXG4gICAgcmVzLnNldEhlYWRlcihcIkFjY2Vzcy1Db250cm9sLUFsbG93LU9yaWdpblwiLCBvcmlnaW4gfHwgXCIqXCIpO1xuXG4gICAgaWYgKHR5cGVvZiB1cmwgIT09IFwic3RyaW5nXCIpXG4gICAgICByZXR1cm4gcmVzXG4gICAgICAgIC5zdGF0dXMoNDAwKVxuICAgICAgICAuanNvbih7IGVycm9yOiBcIkludmFsaWQgdXJsXCIsIGRhdGE6IFtdLCBuZXh0OiBudWxsIH0pO1xuXG4gICAgY29uc3QgcGFyc2VkVVJMID0gYCR7cHJvY2Vzcy5lbnYuQVBJX1VSTH0/dXJsPSR7ZW5jb2RlVVJJQ29tcG9uZW50KFxuICAgICAgdXJsXG4gICAgKX0mbmV4dEluZGV4PSR7bmV4dEluZGV4fSZhY3RpdmVUb3BpYz0ke2FjdGl2ZVRvcGljfSZhY3RpdmVOYXZJbmRleD0wJnRvcGljRW5nTmFtZT0ke2FjdGl2ZVRvcGljfWA7XG4gICAgY29uc3QgcmVzcG9uc2UgPSBhd2FpdCBmZXRjaChwYXJzZWRVUkwpO1xuICAgIGNvbnN0IGpzb24gPSBhd2FpdCByZXNwb25zZS5qc29uKCk7XG5cbiAgICByZXMuc3RhdHVzKDIwMCkuanNvbih7XG4gICAgICBkYXRhOiBqc29uPy5kYXRhPy5yb3dzIHx8IFtdLFxuICAgICAgbmV4dDoganNvbj8udXJsIHx8IG51bGwsXG4gICAgICBuZXh0SW5kZXg6IGpzb24/Lm5leHRJbmRleCB8fCBudWxsLFxuICAgICAgYWN0aXZlVG9waWM6IGpzb24/LmFjdGl2ZVRvcGljIHx8IG51bGwsXG4gICAgfSk7XG4gIH0gY2F0Y2ggKGVycikge1xuICAgIGNvbnNvbGUubG9nKGVycik7XG4gICAgcmVzLnN0YXR1cyg1MDApO1xuICB9XG59XG4iXSwibmFtZXMiOlsiQUxMT1dFRF9PUklHSU5TIiwiaGFuZGxlciIsInJlcSIsInJlcyIsInVybCIsIm5leHRJbmRleCIsImFjdGl2ZVRvcGljIiwiYm9keSIsIm9yaWdpbiIsImhlYWRlcnMiLCJpbmRleE9mIiwic3RhdHVzIiwianNvbiIsImRhdGEiLCJlcnJvciIsIm5leHQiLCJzZXRIZWFkZXIiLCJwYXJzZWRVUkwiLCJwcm9jZXNzIiwiZW52IiwiQVBJX1VSTCIsImVuY29kZVVSSUNvbXBvbmVudCIsInJlc3BvbnNlIiwiZmV0Y2giLCJyb3dzIiwiZXJyIiwiY29uc29sZSIsImxvZyJdLCJzb3VyY2VSb290IjoiIn0=\n//# sourceURL=webpack-internal:///(api)/./pages/api/next.ts\n");

/***/ })

};
;

// load runtime
var __webpack_require__ = require("../../webpack-api-runtime.js");
__webpack_require__.C(exports);
var __webpack_exec__ = (moduleId) => (__webpack_require__(__webpack_require__.s = moduleId))
var __webpack_exports__ = (__webpack_exec__("(api)/./pages/api/next.ts"));
module.exports = __webpack_exports__;

})();