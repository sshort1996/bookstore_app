To get started with MySQL in Python, you can follow these steps:

1. **Install MySQL Connector/Python**: First, you need to install the MySQL Connector/Python library, which allows Python programs to connect to and interact with a MySQL database. You can install it using pip by running the following command:
   ```
   pip install mysql-connector-python
   ```

2. **Import the MySQL Connector module**: In your Python script or program, import the MySQL Connector module using the `import` statement:
   ```python
   import mysql.connector
   ```

3. **Establish a connection to the MySQL database**: To connect to a MySQL database, you need to create a connection object. Provide the necessary database connection details such as hostname, username, password, and database name:
   ```python
   mydb = mysql.connector.connect(
     host="your_host",
     user="your_username",
     password="your_password",
     database="your_database"
   )
   ```

4. **Create a cursor object**: Once the connection is established, create a cursor object, which will allow you to execute SQL statements on the database:
   ```python
   cursor = mydb.cursor()
   ```

5. **Execute SQL queries**: You can now execute SQL queries by calling the `execute()` method of the cursor object. For example, to fetch all rows from a table named "users":
   ```python
   cursor.execute("SELECT * FROM users")
   rows = cursor.fetchall()
   for row in rows:
     print(row)
   ```

6. **Close the connection**: After you have finished working with the database, remember to close the connection:
   ```python
   mydb.close()
   ```

These are the basic steps to get started with MySQL in Python. Make sure you have a MySQL server installed and running, and that you have the necessary credentials to connect to the database. Refer to the MySQL Connector/Python documentation for more advanced usage and examples.


## `mysql` database setup
1: Action 16:42:57: INSTALL. 
1: 1: MySQL Server 8.0 2: {2BA0CF0C-6B36-4A18-8C4E-6086D9DC0DE3} 
1: Action 16:42:57: FindRelatedProducts. Searching for related applications
1: Action 16:42:57: AppSearch. Searching for installed applications
1: Action 16:42:57: DwordToNumber. 
1: Action 16:42:57: LaunchConditions. Evaluating launch conditions
1: Action 16:42:57: ValidateProductID. 
1: Action 16:42:57: CostInitialize. Computing space requirements
1: Action 16:42:57: FileCost. Computing space requirements
1: Action 16:42:57: CostFinalize. Computing space requirements
1: Action 16:42:57: MigrateFeatureStates. Migrating feature states from related applications
1: Action 16:42:57: InstallValidate. Validating install
1: Action 16:42:57: SaveTargetDir. 
1: Action 16:42:57: InstallInitialize. 
1: Action 16:42:57: SetQtRemoveService. 
1: Action 16:42:57: RemoveExistingProducts. Removing applications
1: Action 16:42:57: ProcessComponents. Updating component registration
1: Action 16:42:57: GenerateScript. Generating script operations for action:
1: Updating component registration
1: Action 16:42:57: UnpublishFeatures. Unpublishing Product Features
1: Action 16:42:57: RemoveRegistryValues. Removing system registry values
1: Action 16:42:57: RemoveShortcuts. Removing shortcuts
1: Action 16:42:57: RemoveFiles. Removing files
1: Action 16:42:57: InstallFiles. Copying new files
1: File: Copying new files,  Directory: ,  Size: 
1: Action 16:42:57: CreateShortcuts. Creating shortcuts
1: Shortcut: Creating shortcuts
1: Action 16:42:57: WriteRegistryValues. Writing system registry values
1: Key: Writing system registry values, Name: , Value: 
1: Action 16:42:57: RegisterUser. Registering user
1: Action 16:42:57: RegisterProduct. Registering product
1: Registering product
1: Action 16:42:57: PublishFeatures. Publishing Product Features
1: Feature: Publishing Product Features
1: Action 16:42:57: PublishProduct. Publishing product information
1: Action 16:42:57: InstallFinalize. 
1: Action 16:42:57: ProcessComponents. Updating component registration
1: Action 16:42:58: InstallFiles. Copying new files
1: File: comerr64.dll,  Directory: C:\Program Files\MySQL\MySQL Server 8.0\bin\,  Size: 15872
1: File: fido2.dll,  Directory: C:\Program Files\MySQL\MySQL Server 8.0\bin\,  Size: 233472
1: File: fido2.lib,  Directory: C:\Program Files\MySQL\MySQL Server 8.0\bin\,  Size: 54418
1: File: gssapi64.dll,  Directory: C:\Program Files\MySQL\MySQL Server 8.0\bin\,  Size: 390144
1: File: harness-library.dll,  Directory: C:\Program Files\MySQL\MySQL Server 8.0\bin\,  Size: 797184
1: File: ibd2sdi.exe,  Directory: C:\Program Files\MySQL\MySQL Server 8.0\bin\,  Size: 6422600
1: File: innochecksum.exe,  Directory: C:\Program Files\MySQL\MySQL Server 8.0\bin\,  Size: 6412368
1: File: jemalloc.dll,  Directory: C:\Program Files\MySQL\MySQL Server 8.0\bin\,  Size: 269312
1: File: k5sprt64.dll,  Directory: C:\Program Files\MySQL\MySQL Server 8.0\bin\,  Size: 64000
1: File: krb5_64.dll,  Directory: C:\Program Files\MySQL\MySQL Server 8.0\bin\,  Size: 1223168
1: File: krbcc64.dll,  Directory: C:\Program Files\MySQL\MySQL Server 8.0\bin\,  Size: 112128
1: File: libcrypto-3-x64.dll,  Directory: C:\Program Files\MySQL\MySQL Server 8.0\bin\,  Size: 5151232
1: File: libmecab.dll,  Directory: C:\Program Files\MySQL\MySQL Server 8.0\bin\,  Size: 1839616
1: File: libprotobuf.dll,  Directory: C:\Program Files\MySQL\MySQL Server 8.0\bin\,  Size: 2844672
1: File: libprotobuf.lib,  Directory: C:\Program Files\MySQL\MySQL Server 8.0\bin\,  Size: 3976168
1: File: libprotobuf-debug.dll,  Directory: C:\Program Files\MySQL\MySQL Server 8.0\bin\,  Size: 6142464
1: File: libprotobuf-lite.dll,  Directory: C:\Program Files\MySQL\MySQL Server 8.0\bin\,  Size: 598528
1: File: libprotobuf-lite.lib,  Directory: C:\Program Files\MySQL\MySQL Server 8.0\bin\,  Size: 943314
1: File: libprotobuf-lite-debug.dll,  Directory: C:\Program Files\MySQL\MySQL Server 8.0\bin\,  Size: 1390592
1: File: libsasl.dll,  Directory: C:\Program Files\MySQL\MySQL Server 8.0\bin\,  Size: 110592
1: File: libssl-3-x64.dll,  Directory: C:\Program Files\MySQL\MySQL Server 8.0\bin\,  Size: 777728
1: File: lz4_decompress.exe,  Directory: C:\Program Files\MySQL\MySQL Server 8.0\bin\,  Size: 6353488
1: File: my_print_defaults.exe,  Directory: C:\Program Files\MySQL\MySQL Server 8.0\bin\,  Size: 6287448
1: File: myisam_ftdump.exe,  Directory: C:\Program Files\MySQL\MySQL Server 8.0\bin\,  Size: 6544976
1: File: myisamchk.exe,  Directory: C:\Program Files\MySQL\MySQL Server 8.0\bin\,  Size: 6661704
1: File: myisamlog.exe,  Directory: C:\Program Files\MySQL\MySQL Server 8.0\bin\,  Size: 6504520
1: File: myisampack.exe,  Directory: C:\Program Files\MySQL\MySQL Server 8.0\bin\,  Size: 6566984
1: File: mysql.exe,  Directory: C:\Program Files\MySQL\MySQL Server 8.0\bin\,  Size: 7125568
1: File: mysql_config_editor.exe,  Directory: C:\Program Files\MySQL\MySQL Server 8.0\bin\,  Size: 6301792
1: File: mysql_migrate_keyring.exe,  Directory: C:\Program Files\MySQL\MySQL Server 8.0\bin\,  Size: 7094880
1: File: mysql_secure_installation.exe,  Directory: C:\Program Files\MySQL\MySQL Server 8.0\bin\,  Size: 6999144
1: File: mysql_ssl_rsa_setup.exe,  Directory: C:\Program Files\MySQL\MySQL Server 8.0\bin\,  Size: 6326880
1: File: mysql_tzinfo_to_sql.exe,  Directory: C:\Program Files\MySQL\MySQL Server 8.0\bin\,  Size: 6233696
1: File: mysql_upgrade.exe,  Directory: C:\Program Files\MySQL\MySQL Server 8.0\bin\,  Size: 7098448
1: File: mysqladmin.exe,  Directory: C:\Program Files\MySQL\MySQL Server 8.0\bin\,  Size: 7012432
1: File: mysqlbinlog.exe,  Directory: C:\Program Files\MySQL\MySQL Server 8.0\bin\,  Size: 7394384
1: File: mysqlcheck.exe,  Directory: C:\Program Files\MySQL\MySQL Server 8.0\bin\,  Size: 7018064
1: File: mysqld.exe,  Directory: C:\Program Files\MySQL\MySQL Server 8.0\bin\,  Size: 54166600
1: File: mysqld_multi.pl,  Directory: C:\Program Files\MySQL\MySQL Server 8.0\bin\,  Size: 28776
1: File: mysqldump.exe,  Directory: C:\Program Files\MySQL\MySQL Server 8.0\bin\,  Size: 7085128
1: File: mysqldumpslow.pl,  Directory: C:\Program Files\MySQL\MySQL Server 8.0\bin\,  Size: 7881
1: File: mysqlharness_stdx.dll,  Directory: C:\Program Files\MySQL\MySQL Server 8.0\bin\,  Size: 42072
1: File: mysqlharness_tls.dll,  Directory: C:\Program Files\MySQL\MySQL Server 8.0\bin\,  Size: 69208
1: File: mysqlimport.exe,  Directory: C:\Program Files\MySQL\MySQL Server 8.0\bin\,  Size: 7005264
1: File: mysqlpump.exe,  Directory: C:\Program Files\MySQL\MySQL Server 8.0\bin\,  Size: 7520840
1: File: mysqlrouter.exe,  Directory: C:\Program Files\MySQL\MySQL Server 8.0\bin\,  Size: 7529040
1: File: mysqlrouter_connection_pool.dll,  Directory: C:\Program Files\MySQL\MySQL Server 8.0\bin\,  Size: 72304
1: File: mysqlrouter_destination_status.dll,  Directory: C:\Program Files\MySQL\MySQL Server 8.0\bin\,  Size: 97904
1: File: mysqlrouter_http.dll,  Directory: C:\Program Files\MySQL\MySQL Server 8.0\bin\,  Size: 272472
1: File: mysqlrouter_http_auth_backend.dll,  Directory: C:\Program Files\MySQL\MySQL Server 8.0\bin\,  Size: 115312
1: File: mysqlrouter_http_auth_realm.dll,  Directory: C:\Program Files\MySQL\MySQL Server 8.0\bin\,  Size: 38512
1: File: mysqlrouter_io_component.dll,  Directory: C:\Program Files\MySQL\MySQL Server 8.0\bin\,  Size: 6273640
1: File: mysqlrouter_keyring.exe,  Directory: C:\Program Files\MySQL\MySQL Server 8.0\bin\,  Size: 6313568
1: File: mysqlrouter_lib.dll,  Directory: C:\Program Files\MySQL\MySQL Server 8.0\bin\,  Size: 7311448
1: File: mysqlrouter_metadata_cache.dll,  Directory: C:\Program Files\MySQL\MySQL Server 8.0\bin\,  Size: 7863400
1: File: mysqlrouter_passwd.exe,  Directory: C:\Program Files\MySQL\MySQL Server 8.0\bin\,  Size: 6284896
1: File: mysqlrouter_plugin_info.exe,  Directory: C:\Program Files\MySQL\MySQL Server 8.0\bin\,  Size: 6269032
1: File: mysqlrouter_routing.dll,  Directory: C:\Program Files\MySQL\MySQL Server 8.0\bin\,  Size: 7343712
1: File: mysqlshow.exe,  Directory: C:\Program Files\MySQL\MySQL Server 8.0\bin\,  Size: 7002184
1: File: mysqlslap.exe,  Directory: C:\Program Files\MySQL\MySQL Server 8.0\bin\,  Size: 7021640
1: File: perror.exe,  Directory: C:\Program Files\MySQL\MySQL Server 8.0\bin\,  Size: 7176264
1: File: saslSCRAM.dll,  Directory: C:\Program Files\MySQL\MySQL Server 8.0\bin\,  Size: 47104
1: File: xpprof64.dll,  Directory: C:\Program Files\MySQL\MySQL Server 8.0\bin\,  Size: 48128
1: File: zlib_decompress.exe,  Directory: C:\Program Files\MySQL\MySQL Server 8.0\bin\,  Size: 6253144
1: File: INFO_BIN,  Directory: C:\Program Files\MySQL\MySQL Server 8.0\docs\,  Size: 10980
1: File: INFO_SRC,  Directory: C:\Program Files\MySQL\MySQL Server 8.0\docs\,  Size: 188
1: File: sample_mysqlrouter.conf,  Directory: C:\Program Files\MySQL\MySQL Server 8.0\docs\,  Size: 2213
1: File: mysqlrouter.conf.sample,  Directory: C:\Program Files\MySQL\MySQL Server 8.0\etc\,  Size: 1672
1: File: errmsg.h,  Directory: C:\Program Files\MySQL\MySQL Server 8.0\include\,  Size: 5730
1: File: field_types.h,  Directory: C:\Program Files\MySQL\MySQL Server 8.0\include\,  Size: 3030
1: File: my_command.h,  Directory: C:\Program Files\MySQL\MySQL Server 8.0\include\,  Size: 4407
1: File: my_compress.h,  Directory: C:\Program Files\MySQL\MySQL Server 8.0\include\,  Size: 3646
1: File: my_list.h,  Directory: C:\Program Files\MySQL\MySQL Server 8.0\include\,  Size: 2069
1: File: mysql.h,  Directory: C:\Program Files\MySQL\MySQL Server 8.0\include\,  Size: 33483
1: File: client_plugin.h,  Directory: C:\Program Files\MySQL\MySQL Server 8.0\include\mysql\,  Size: 8354
1: File: mysql_com.h,  Directory: C:\Program Files\MySQL\MySQL Server 8.0\include\,  Size: 37337
1: File: plugin_auth_common.h,  Directory: C:\Program Files\MySQL\MySQL Server 8.0\include\mysql\,  Size: 6866
1: File: mysql_time.h,  Directory: C:\Program Files\MySQL\MySQL Server 8.0\include\,  Size: 3554
1: File: udf_registration_types.h,  Directory: C:\Program Files\MySQL\MySQL Server 8.0\include\mysql\,  Size: 3827
1: File: mysql_version.h,  Directory: C:\Program Files\MySQL\MySQL Server 8.0\include\,  Size: 1120
1: File: mysqld_error.h,  Directory: C:\Program Files\MySQL\MySQL Server 8.0\include\,  Size: 267073
1: File: mysqlx_ername.h,  Directory: C:\Program Files\MySQL\MySQL Server 8.0\include\,  Size: 7304
1: File: mysqlx_error.h,  Directory: C:\Program Files\MySQL\MySQL Server 8.0\include\,  Size: 4211
1: File: mysqlx_version.h,  Directory: C:\Program Files\MySQL\MySQL Server 8.0\include\,  Size: 1840
1: File: applink.c,  Directory: C:\Program Files\MySQL\MySQL Server 8.0\include\openssl\,  Size: 3660
1: File: connection_pool.dll,  Directory: C:\Program Files\MySQL\MySQL Server 8.0\lib\,  Size: 35840
1: File: destination_status.dll,  Directory: C:\Program Files\MySQL\MySQL Server 8.0\lib\,  Size: 31232
1: File: http_auth_backend.dll,  Directory: C:\Program Files\MySQL\MySQL Server 8.0\lib\,  Size: 42496
1: File: http_auth_realm.dll,  Directory: C:\Program Files\MySQL\MySQL Server 8.0\lib\,  Size: 45056
1: File: http_server.dll,  Directory: C:\Program Files\MySQL\MySQL Server 8.0\lib\,  Size: 6396928
1: File: io.dll,  Directory: C:\Program Files\MySQL\MySQL Server 8.0\lib\,  Size: 6234112
1: File: keepalive.dll,  Directory: C:\Program Files\MySQL\MySQL Server 8.0\lib\,  Size: 19456
1: File: libmysql.dll,  Directory: C:\Program Files\MySQL\MySQL Server 8.0\lib\,  Size: 6978560
1: File: libmysql.lib,  Directory: C:\Program Files\MySQL\MySQL Server 8.0\lib\,  Size: 31320
1: File: libprotobuf-lite.dll,  Directory: C:\Program Files\MySQL\MySQL Server 8.0\lib\,  Size: 598528
1: File: libprotobuf-lite.lib,  Directory: C:\Program Files\MySQL\MySQL Server 8.0\lib\,  Size: 943314
1: File: char.bin,  Directory: C:\Program Files\MySQL\MySQL Server 8.0\lib\mecab\dic\ipadic_euc-jp\,  Size: 262496
1: File: dicrc,  Directory: C:\Program Files\MySQL\MySQL Server 8.0\lib\mecab\dic\ipadic_euc-jp\,  Size: 693
1: File: left-id.def,  Directory: C:\Program Files\MySQL\MySQL Server 8.0\lib\mecab\dic\ipadic_euc-jp\,  Size: 55910
1: File: matrix.bin,  Directory: C:\Program Files\MySQL\MySQL Server 8.0\lib\mecab\dic\ipadic_euc-jp\,  Size: 3463716
1: File: pos-id.def,  Directory: C:\Program Files\MySQL\MySQL Server 8.0\lib\mecab\dic\ipadic_euc-jp\,  Size: 1477
1: File: rewrite.def,  Directory: C:\Program Files\MySQL\MySQL Server 8.0\lib\mecab\dic\ipadic_euc-jp\,  Size: 6241
1: File: right-id.def,  Directory: C:\Program Files\MySQL\MySQL Server 8.0\lib\mecab\dic\ipadic_euc-jp\,  Size: 55910
1: File: sys.dic,  Directory: C:\Program Files\MySQL\MySQL Server 8.0\lib\mecab\dic\ipadic_euc-jp\,  Size: 37779919
1: File: unk.dic,  Directory: C:\Program Files\MySQL\MySQL Server 8.0\lib\mecab\dic\ipadic_euc-jp\,  Size: 5409
1: File: char.bin,  Directory: C:\Program Files\MySQL\MySQL Server 8.0\lib\mecab\dic\ipadic_sjis\,  Size: 262496
1: File: dicrc,  Directory: C:\Program Files\MySQL\MySQL Server 8.0\lib\mecab\dic\ipadic_sjis\,  Size: 693
1: File: left-id.def,  Directory: C:\Program Files\MySQL\MySQL Server 8.0\lib\mecab\dic\ipadic_sjis\,  Size: 55910
1: File: matrix.bin,  Directory: C:\Program Files\MySQL\MySQL Server 8.0\lib\mecab\dic\ipadic_sjis\,  Size: 3463716
1: File: pos-id.def,  Directory: C:\Program Files\MySQL\MySQL Server 8.0\lib\mecab\dic\ipadic_sjis\,  Size: 1477
1: File: rewrite.def,  Directory: C:\Program Files\MySQL\MySQL Server 8.0\lib\mecab\dic\ipadic_sjis\,  Size: 6241
1: File: right-id.def,  Directory: C:\Program Files\MySQL\MySQL Server 8.0\lib\mecab\dic\ipadic_sjis\,  Size: 55910
1: File: sys.dic,  Directory: C:\Program Files\MySQL\MySQL Server 8.0\lib\mecab\dic\ipadic_sjis\,  Size: 37635899
1: File: unk.dic,  Directory: C:\Program Files\MySQL\MySQL Server 8.0\lib\mecab\dic\ipadic_sjis\,  Size: 5409
1: File: char.bin,  Directory: C:\Program Files\MySQL\MySQL Server 8.0\lib\mecab\dic\ipadic_utf-8\,  Size: 262496
1: File: dicrc,  Directory: C:\Program Files\MySQL\MySQL Server 8.0\lib\mecab\dic\ipadic_utf-8\,  Size: 693
1: File: left-id.def,  Directory: C:\Program Files\MySQL\MySQL Server 8.0\lib\mecab\dic\ipadic_utf-8\,  Size: 55910
1: File: matrix.bin,  Directory: C:\Program Files\MySQL\MySQL Server 8.0\lib\mecab\dic\ipadic_utf-8\,  Size: 3463716
1: File: pos-id.def,  Directory: C:\Program Files\MySQL\MySQL Server 8.0\lib\mecab\dic\ipadic_utf-8\,  Size: 1477
1: File: rewrite.def,  Directory: C:\Program Files\MySQL\MySQL Server 8.0\lib\mecab\dic\ipadic_utf-8\,  Size: 6241
1: File: right-id.def,  Directory: C:\Program Files\MySQL\MySQL Server 8.0\lib\mecab\dic\ipadic_utf-8\,  Size: 55910
1: File: sys.dic,  Directory: C:\Program Files\MySQL\MySQL Server 8.0\lib\mecab\dic\ipadic_utf-8\,  Size: 49199027
1: File: unk.dic,  Directory: C:\Program Files\MySQL\MySQL Server 8.0\lib\mecab\dic\ipadic_utf-8\,  Size: 5690
1: File: mecabrc,  Directory: C:\Program Files\MySQL\MySQL Server 8.0\lib\mecab\etc\,  Size: 1382
1: File: metadata_cache.dll,  Directory: C:\Program Files\MySQL\MySQL Server 8.0\lib\,  Size: 7011328
1: File: mysqlclient.lib,  Directory: C:\Program Files\MySQL\MySQL Server 8.0\lib\,  Size: 44165990
1: File: mysqlharness_stdx.lib,  Directory: C:\Program Files\MySQL\MySQL Server 8.0\lib\,  Size: 10392
1: File: mysqlharness_tls.lib,  Directory: C:\Program Files\MySQL\MySQL Server 8.0\lib\,  Size: 23968
1: File: mysqlrouter_connection_pool.lib,  Directory: C:\Program Files\MySQL\MySQL Server 8.0\lib\,  Size: 27742
1: File: mysqlrouter_destination_status.lib,  Directory: C:\Program Files\MySQL\MySQL Server 8.0\lib\,  Size: 8430
1: File: mysqlrouter_http.lib,  Directory: C:\Program Files\MySQL\MySQL Server 8.0\lib\,  Size: 45804
1: File: mysqlrouter_http_auth_backend.lib,  Directory: C:\Program Files\MySQL\MySQL Server 8.0\lib\,  Size: 48066
1: File: mysqlrouter_http_auth_realm.lib,  Directory: C:\Program Files\MySQL\MySQL Server 8.0\lib\,  Size: 11332
1: File: mysqlrouter_io_component.lib,  Directory: C:\Program Files\MySQL\MySQL Server 8.0\lib\,  Size: 12642
1: File: mysqlrouter_lib.lib,  Directory: C:\Program Files\MySQL\MySQL Server 8.0\lib\,  Size: 116216
1: File: mysqlrouter_metadata_cache.lib,  Directory: C:\Program Files\MySQL\MySQL Server 8.0\lib\,  Size: 108418
1: File: mysqlrouter_mysqlxmessages.dll,  Directory: C:\Program Files\MySQL\MySQL Server 8.0\lib\,  Size: 150016
1: File: mysqlrouter_mysqlxmessages.lib,  Directory: C:\Program Files\MySQL\MySQL Server 8.0\lib\,  Size: 2158
1: File: mysqlrouter_routing.lib,  Directory: C:\Program Files\MySQL\MySQL Server 8.0\lib\,  Size: 51138
1: File: adt_null.dll,  Directory: C:\Program Files\MySQL\MySQL Server 8.0\lib\plugin\,  Size: 26112
1: File: authentication_fido_client.dll,  Directory: C:\Program Files\MySQL\MySQL Server 8.0\lib\plugin\,  Size: 31232
1: File: authentication_kerberos_client.dll,  Directory: C:\Program Files\MySQL\MySQL Server 8.0\lib\plugin\,  Size: 6258688
1: File: authentication_ldap_sasl_client.dll,  Directory: C:\Program Files\MySQL\MySQL Server 8.0\lib\plugin\,  Size: 44032
1: File: authentication_oci_client.dll,  Directory: C:\Program Files\MySQL\MySQL Server 8.0\lib\plugin\,  Size: 6306304
1: File: component_audit_api_message_emit.dll,  Directory: C:\Program Files\MySQL\MySQL Server 8.0\lib\plugin\,  Size: 24576
1: File: component_keyring_file.dll,  Directory: C:\Program Files\MySQL\MySQL Server 8.0\lib\plugin\,  Size: 1221632
1: File: component_log_filter_dragnet.dll,  Directory: C:\Program Files\MySQL\MySQL Server 8.0\lib\plugin\,  Size: 32256
1: File: component_log_sink_json.dll,  Directory: C:\Program Files\MySQL\MySQL Server 8.0\lib\plugin\,  Size: 36352
1: File: component_log_sink_syseventlog.dll,  Directory: C:\Program Files\MySQL\MySQL Server 8.0\lib\plugin\,  Size: 17920
1: File: component_mysqlbackup.dll,  Directory: C:\Program Files\MySQL\MySQL Server 8.0\lib\plugin\,  Size: 44032
1: File: component_query_attributes.dll,  Directory: C:\Program Files\MySQL\MySQL Server 8.0\lib\plugin\,  Size: 14336
1: File: component_reference_cache.dll,  Directory: C:\Program Files\MySQL\MySQL Server 8.0\lib\plugin\,  Size: 45568
1: File: component_validate_password.dll,  Directory: C:\Program Files\MySQL\MySQL Server 8.0\lib\plugin\,  Size: 68096
1: File: connection_control.dll,  Directory: C:\Program Files\MySQL\MySQL Server 8.0\lib\plugin\,  Size: 45568
1: File: ddl_rewriter.dll,  Directory: C:\Program Files\MySQL\MySQL Server 8.0\lib\plugin\,  Size: 71168
1: File: group_replication.dll,  Directory: C:\Program Files\MySQL\MySQL Server 8.0\lib\plugin\,  Size: 1939968
1: File: ha_example.dll,  Directory: C:\Program Files\MySQL\MySQL Server 8.0\lib\plugin\,  Size: 30720
1: File: ha_mock.dll,  Directory: C:\Program Files\MySQL\MySQL Server 8.0\lib\plugin\,  Size: 40448
1: File: keyring_file.dll,  Directory: C:\Program Files\MySQL\MySQL Server 8.0\lib\plugin\,  Size: 94208
1: File: keyring_udf.dll,  Directory: C:\Program Files\MySQL\MySQL Server 8.0\lib\plugin\,  Size: 26624
1: File: libpluginmecab.dll,  Directory: C:\Program Files\MySQL\MySQL Server 8.0\lib\plugin\,  Size: 30720
1: File: locking_service.dll,  Directory: C:\Program Files\MySQL\MySQL Server 8.0\lib\plugin\,  Size: 13824
1: File: mypluglib.dll,  Directory: C:\Program Files\MySQL\MySQL Server 8.0\lib\plugin\,  Size: 14336
1: File: mysql_clone.dll,  Directory: C:\Program Files\MySQL\MySQL Server 8.0\lib\plugin\,  Size: 142336
1: File: mysql_no_login.dll,  Directory: C:\Program Files\MySQL\MySQL Server 8.0\lib\plugin\,  Size: 12288
1: File: rewrite_example.dll,  Directory: C:\Program Files\MySQL\MySQL Server 8.0\lib\plugin\,  Size: 13824
1: File: rewriter.dll,  Directory: C:\Program Files\MySQL\MySQL Server 8.0\lib\plugin\,  Size: 59904
1: File: semisync_master.dll,  Directory: C:\Program Files\MySQL\MySQL Server 8.0\lib\plugin\,  Size: 79360
1: File: semisync_replica.dll,  Directory: C:\Program Files\MySQL\MySQL Server 8.0\lib\plugin\,  Size: 35328
1: File: semisync_slave.dll,  Directory: C:\Program Files\MySQL\MySQL Server 8.0\lib\plugin\,  Size: 35840
1: File: semisync_source.dll,  Directory: C:\Program Files\MySQL\MySQL Server 8.0\lib\plugin\,  Size: 78336
1: File: validate_password.dll,  Directory: C:\Program Files\MySQL\MySQL Server 8.0\lib\plugin\,  Size: 47616
1: File: version_token.dll,  Directory: C:\Program Files\MySQL\MySQL Server 8.0\lib\plugin\,  Size: 50688
1: File: burmesedict.dict,  Directory: C:\Program Files\MySQL\MySQL Server 8.0\lib\private\icudt73l\brkitr\,  Size: 254448
1: File: char.brk,  Directory: C:\Program Files\MySQL\MySQL Server 8.0\lib\private\icudt73l\brkitr\,  Size: 13776
1: File: cjdict.dict,  Directory: C:\Program Files\MySQL\MySQL Server 8.0\lib\private\icudt73l\brkitr\,  Size: 2007296
1: File: de.res,  Directory: C:\Program Files\MySQL\MySQL Server 8.0\lib\private\icudt73l\brkitr\,  Size: 2992
1: File: el.res,  Directory: C:\Program Files\MySQL\MySQL Server 8.0\lib\private\icudt73l\brkitr\,  Size: 160
1: File: en.res,  Directory: C:\Program Files\MySQL\MySQL Server 8.0\lib\private\icudt73l\brkitr\,  Size: 1776
1: File: en_US.res,  Directory: C:\Program Files\MySQL\MySQL Server 8.0\lib\private\icudt73l\brkitr\,  Size: 80
1: File: en_US_POSIX.res,  Directory: C:\Program Files\MySQL\MySQL Server 8.0\lib\private\icudt73l\brkitr\,  Size: 160
1: File: es.res,  Directory: C:\Program Files\MySQL\MySQL Server 8.0\lib\private\icudt73l\brkitr\,  Size: 2176
1: File: fi.res,  Directory: C:\Program Files\MySQL\MySQL Server 8.0\lib\private\icudt73l\brkitr\,  Size: 160
1: File: fr.res,  Directory: C:\Program Files\MySQL\MySQL Server 8.0\lib\private\icudt73l\brkitr\,  Size: 1200
1: File: it.res,  Directory: C:\Program Files\MySQL\MySQL Server 8.0\lib\private\icudt73l\brkitr\,  Size: 688
1: File: ja.res,  Directory: C:\Program Files\MySQL\MySQL Server 8.0\lib\private\icudt73l\brkitr\,  Size: 2784
1: File: khmerdict.dict,  Directory: C:\Program Files\MySQL\MySQL Server 8.0\lib\private\icudt73l\brkitr\,  Size: 445552
1: File: ko.res,  Directory: C:\Program Files\MySQL\MySQL Server 8.0\lib\private\icudt73l\brkitr\,  Size: 544
1: File: laodict.dict,  Directory: C:\Program Files\MySQL\MySQL Server 8.0\lib\private\icudt73l\brkitr\,  Size: 162624
1: File: line.brk,  Directory: C:\Program Files\MySQL\MySQL Server 8.0\lib\private\icudt73l\brkitr\,  Size: 24896
1: File: line_cj.brk,  Directory: C:\Program Files\MySQL\MySQL Server 8.0\lib\private\icudt73l\brkitr\,  Size: 24928
1: File: line_loose.brk,  Directory: C:\Program Files\MySQL\MySQL Server 8.0\lib\private\icudt73l\brkitr\,  Size: 25056
1: File: line_loose_cj.brk,  Directory: C:\Program Files\MySQL\MySQL Server 8.0\lib\private\icudt73l\brkitr\,  Size: 26080
1: File: line_loose_phrase_cj.brk,  Directory: C:\Program Files\MySQL\MySQL Server 8.0\lib\private\icudt73l\brkitr\,  Size: 28048
1: File: line_normal.brk,  Directory: C:\Program Files\MySQL\MySQL Server 8.0\lib\private\icudt73l\brkitr\,  Size: 24720
1: File: line_normal_cj.brk,  Directory: C:\Program Files\MySQL\MySQL Server 8.0\lib\private\icudt73l\brkitr\,  Size: 24912
1: File: line_normal_phrase_cj.brk,  Directory: C:\Program Files\MySQL\MySQL Server 8.0\lib\private\icudt73l\brkitr\,  Size: 26816
1: File: line_phrase_cj.brk,  Directory: C:\Program Files\MySQL\MySQL Server 8.0\lib\private\icudt73l\brkitr\,  Size: 26752
1: File: pt.res,  Directory: C:\Program Files\MySQL\MySQL Server 8.0\lib\private\icudt73l\brkitr\,  Size: 2288
1: File: res_index.res,  Directory: C:\Program Files\MySQL\MySQL Server 8.0\lib\private\icudt73l\brkitr\,  Size: 240
1: File: root.res,  Directory: C:\Program Files\MySQL\MySQL Server 8.0\lib\private\icudt73l\brkitr\,  Size: 800
1: File: ru.res,  Directory: C:\Program Files\MySQL\MySQL Server 8.0\lib\private\icudt73l\brkitr\,  Size: 336
1: File: sent.brk,  Directory: C:\Program Files\MySQL\MySQL Server 8.0\lib\private\icudt73l\brkitr\,  Size: 19648
1: File: sent_el.brk,  Directory: C:\Program Files\MySQL\MySQL Server 8.0\lib\private\icudt73l\brkitr\,  Size: 19664
1: File: sv.res,  Directory: C:\Program Files\MySQL\MySQL Server 8.0\lib\private\icudt73l\brkitr\,  Size: 160
1: File: thaidict.dict,  Directory: C:\Program Files\MySQL\MySQL Server 8.0\lib\private\icudt73l\brkitr\,  Size: 126144
1: File: title.brk,  Directory: C:\Program Files\MySQL\MySQL Server 8.0\lib\private\icudt73l\brkitr\,  Size: 12112
1: File: word.brk,  Directory: C:\Program Files\MySQL\MySQL Server 8.0\lib\private\icudt73l\brkitr\,  Size: 22592
1: File: word_fi_sv.brk,  Directory: C:\Program Files\MySQL\MySQL Server 8.0\lib\private\icudt73l\brkitr\,  Size: 22576
1: File: word_POSIX.brk,  Directory: C:\Program Files\MySQL\MySQL Server 8.0\lib\private\icudt73l\brkitr\,  Size: 22608
1: File: zh.res,  Directory: C:\Program Files\MySQL\MySQL Server 8.0\lib\private\icudt73l\brkitr\,  Size: 272
1: File: zh_Hant.res,  Directory: C:\Program Files\MySQL\MySQL Server 8.0\lib\private\icudt73l\brkitr\,  Size: 272
1: File: cnvalias.icu,  Directory: C:\Program Files\MySQL\MySQL Server 8.0\lib\private\icudt73l\,  Size: 63984
1: File: uemoji.icu,  Directory: C:\Program Files\MySQL\MySQL Server 8.0\lib\private\icudt73l\,  Size: 13024
1: File: ulayout.icu,  Directory: C:\Program Files\MySQL\MySQL Server 8.0\lib\private\icudt73l\,  Size: 13728
1: File: unames.icu,  Directory: C:\Program Files\MySQL\MySQL Server 8.0\lib\private\icudt73l\,  Size: 296000
1: File: rest_api.dll,  Directory: C:\Program Files\MySQL\MySQL Server 8.0\lib\,  Size: 142848
1: File: rest_connection_pool.dll,  Directory: C:\Program Files\MySQL\MySQL Server 8.0\lib\,  Size: 95232
1: File: rest_metadata_cache.dll,  Directory: C:\Program Files\MySQL\MySQL Server 8.0\lib\,  Size: 112640
1: File: rest_router.dll,  Directory: C:\Program Files\MySQL\MySQL Server 8.0\lib\,  Size: 80896
1: File: rest_routing.dll,  Directory: C:\Program Files\MySQL\MySQL Server 8.0\lib\,  Size: 131072
1: File: router_openssl.dll,  Directory: C:\Program Files\MySQL\MySQL Server 8.0\lib\,  Size: 14848
1: File: router_protobuf.dll,  Directory: C:\Program Files\MySQL\MySQL Server 8.0\lib\,  Size: 11776
1: File: routing.dll,  Directory: C:\Program Files\MySQL\MySQL Server 8.0\lib\,  Size: 100352
1: File: LICENSE,  Directory: C:\Program Files\MySQL\MySQL Server 8.0\,  Size: 279815
1: File: LICENSE.router,  Directory: C:\Program Files\MySQL\MySQL Server 8.0\,  Size: 114697
1: File: README,  Directory: C:\Program Files\MySQL\MySQL Server 8.0\,  Size: 666
1: File: README.router,  Directory: C:\Program Files\MySQL\MySQL Server 8.0\,  Size: 679
1: File: errmsg.sys,  Directory: C:\Program Files\MySQL\MySQL Server 8.0\share\bulgarian\,  Size: 386036
1: File: armscii8.xml,  Directory: C:\Program Files\MySQL\MySQL Server 8.0\share\charsets\,  Size: 5961
1: File: ascii.xml,  Directory: C:\Program Files\MySQL\MySQL Server 8.0\share\charsets\,  Size: 5947
1: File: cp1250.xml,  Directory: C:\Program Files\MySQL\MySQL Server 8.0\share\charsets\,  Size: 8676
1: File: cp1251.xml,  Directory: C:\Program Files\MySQL\MySQL Server 8.0\share\charsets\,  Size: 8762
1: File: cp1256.xml,  Directory: C:\Program Files\MySQL\MySQL Server 8.0\share\charsets\,  Size: 6010
1: File: cp1257.xml,  Directory: C:\Program Files\MySQL\MySQL Server 8.0\share\charsets\,  Size: 9343
1: File: cp850.xml,  Directory: C:\Program Files\MySQL\MySQL Server 8.0\share\charsets\,  Size: 5947
1: File: cp852.xml,  Directory: C:\Program Files\MySQL\MySQL Server 8.0\share\charsets\,  Size: 5963
1: File: cp866.xml,  Directory: C:\Program Files\MySQL\MySQL Server 8.0\share\charsets\,  Size: 6054
1: File: dec8.xml,  Directory: C:\Program Files\MySQL\MySQL Server 8.0\share\charsets\,  Size: 6970
1: File: geostd8.xml,  Directory: C:\Program Files\MySQL\MySQL Server 8.0\share\charsets\,  Size: 5957
1: File: greek.xml,  Directory: C:\Program Files\MySQL\MySQL Server 8.0\share\charsets\,  Size: 6169
1: File: hebrew.xml,  Directory: C:\Program Files\MySQL\MySQL Server 8.0\share\charsets\,  Size: 5952
1: File: hp8.xml,  Directory: C:\Program Files\MySQL\MySQL Server 8.0\share\charsets\,  Size: 5943
1: File: Index.xml,  Directory: C:\Program Files\MySQL\MySQL Server 8.0\share\charsets\,  Size: 19475
1: File: keybcs2.xml,  Directory: C:\Program Files\MySQL\MySQL Server 8.0\share\charsets\,  Size: 5970
1: File: koi8r.xml,  Directory: C:\Program Files\MySQL\MySQL Server 8.0\share\charsets\,  Size: 5951
1: File: koi8u.xml,  Directory: C:\Program Files\MySQL\MySQL Server 8.0\share\charsets\,  Size: 6973
1: File: latin1.xml,  Directory: C:\Program Files\MySQL\MySQL Server 8.0\share\charsets\,  Size: 10251
1: File: latin2.xml,  Directory: C:\Program Files\MySQL\MySQL Server 8.0\share\charsets\,  Size: 7673
1: File: latin5.xml,  Directory: C:\Program Files\MySQL\MySQL Server 8.0\share\charsets\,  Size: 5950
1: File: latin7.xml,  Directory: C:\Program Files\MySQL\MySQL Server 8.0\share\charsets\,  Size: 7879
1: File: macce.xml,  Directory: C:\Program Files\MySQL\MySQL Server 8.0\share\charsets\,  Size: 8488
1: File: macroman.xml,  Directory: C:\Program Files\MySQL\MySQL Server 8.0\share\charsets\,  Size: 8499
1: File: README,  Directory: C:\Program Files\MySQL\MySQL Server 8.0\share\charsets\,  Size: 1749
1: File: swe7.xml,  Directory: C:\Program Files\MySQL\MySQL Server 8.0\share\charsets\,  Size: 6971
1: File: errmsg.sys,  Directory: C:\Program Files\MySQL\MySQL Server 8.0\share\czech\,  Size: 385958
1: File: errmsg.sys,  Directory: C:\Program Files\MySQL\MySQL Server 8.0\share\danish\,  Size: 385932
1: File: dictionary.txt,  Directory: C:\Program Files\MySQL\MySQL Server 8.0\share\,  Size: 25575
1: File: errmsg.sys,  Directory: C:\Program Files\MySQL\MySQL Server 8.0\share\dutch\,  Size: 386946
1: File: errmsg.sys,  Directory: C:\Program Files\MySQL\MySQL Server 8.0\share\english\,  Size: 385199
1: File: errmsg.sys,  Directory: C:\Program Files\MySQL\MySQL Server 8.0\share\estonian\,  Size: 385463
1: File: errmsg.sys,  Directory: C:\Program Files\MySQL\MySQL Server 8.0\share\french\,  Size: 386572
1: File: errmsg.sys,  Directory: C:\Program Files\MySQL\MySQL Server 8.0\share\german\,  Size: 392773
1: File: errmsg.sys,  Directory: C:\Program Files\MySQL\MySQL Server 8.0\share\greek\,  Size: 391990
1: File: errmsg.sys,  Directory: C:\Program Files\MySQL\MySQL Server 8.0\share\hungarian\,  Size: 385840
1: File: errmsg.sys,  Directory: C:\Program Files\MySQL\MySQL Server 8.0\share\italian\,  Size: 386943
1: File: errmsg.sys,  Directory: C:\Program Files\MySQL\MySQL Server 8.0\share\japanese\,  Size: 392583
1: File: errmsg.sys,  Directory: C:\Program Files\MySQL\MySQL Server 8.0\share\korean\,  Size: 388239
1: File: messages_to_clients.txt,  Directory: C:\Program Files\MySQL\MySQL Server 8.0\share\,  Size: 630189
1: File: messages_to_error_log.txt,  Directory: C:\Program Files\MySQL\MySQL Server 8.0\share\,  Size: 393145
1: File: errmsg.sys,  Directory: C:\Program Files\MySQL\MySQL Server 8.0\share\norwegian\,  Size: 385269
1: File: errmsg.sys,  Directory: C:\Program Files\MySQL\MySQL Server 8.0\share\norwegian-ny\,  Size: 385322
1: File: errmsg.sys,  Directory: C:\Program Files\MySQL\MySQL Server 8.0\share\polish\,  Size: 386128
1: File: errmsg.sys,  Directory: C:\Program Files\MySQL\MySQL Server 8.0\share\portuguese\,  Size: 388105
1: File: errmsg.sys,  Directory: C:\Program Files\MySQL\MySQL Server 8.0\share\romanian\,  Size: 386911
1: File: errmsg.sys,  Directory: C:\Program Files\MySQL\MySQL Server 8.0\share\russian\,  Size: 400399
1: File: errmsg.sys,  Directory: C:\Program Files\MySQL\MySQL Server 8.0\share\serbian\,  Size: 387546
1: File: errmsg.sys,  Directory: C:\Program Files\MySQL\MySQL Server 8.0\share\slovak\,  Size: 385725
1: File: errmsg.sys,  Directory: C:\Program Files\MySQL\MySQL Server 8.0\share\spanish\,  Size: 386799
1: File: errmsg.sys,  Directory: C:\Program Files\MySQL\MySQL Server 8.0\share\swedish\,  Size: 386012
1: File: errmsg.sys,  Directory: C:\Program Files\MySQL\MySQL Server 8.0\share\ukrainian\,  Size: 395022
1: Action 16:43:04: CreateShortcuts. Creating shortcuts
1: Shortcut: icon.ico
1: Shortcut: Icon.MysqlCmdShell
1: Shortcut: rpxm3ds_|MySQL 8.0 Command Line Client
1: Shortcut: 7ejegqmo|MySQL 8.0 Command Line Client - Unicode
1: Action 16:43:04: WriteRegistryValues. Writing system registry values
1: Key: \SOFTWARE\MySQL AB\MySQL Server 8.0, Name: Location, Value: C:\Program Files\MySQL\MySQL Server 8.0\
1: Key: \SOFTWARE\MySQL AB\MySQL Server 8.0, Name: Version, Value: 8.0.34
1: Key: \SOFTWARE\MySQL AB\MySQL Server 8.0, Name: DataLocation, Value: C:\ProgramData\MySQL\MySQL Server 8.0
1: Key: \SOFTWARE\MySQL AB\MySQL Server 8.0, Name: , Value: 
1: Key: \Console\MySQL 8.0 Command Line Client - Unicode, Name: FaceName, Value: Lucida Console
1: Key: \Console\MySQL 8.0 Command Line Client - Unicode, Name: FontWeight, Value: #400
1: Key: \Console\MySQL 8.0 Command Line Client - Unicode, Name: , Value: 
1: Key: \Software\MySQL AB\MySQL Server 8.0, Name: installed, Value: #1
1: Action 16:43:04: RegisterProduct. Registering product
1: {2BA0CF0C-6B36-4A18-8C4E-6086D9DC0DE3}
1: Action 16:43:04: PublishFeatures. Publishing Product Features
1: Feature: RegKeys
1: Feature: Client
1: Feature: MYSQLSERVER
1: Feature: DEVEL
1: Feature: DOCUMENTATION
1: Feature: INFO
1: Feature: Readme
1: Feature: ALWAYSINSTALL
1: Feature: Router
1: Feature: Server_Scripts
1: Feature: MISC
1: Feature: ProgramMenu
1: Action 16:43:04: PublishProduct. Publishing product information
1: Action 16:43:04: RollbackCleanup. Removing backup files
1: 1: MySQL Server 8.0 2: {2BA0CF0C-6B36-4A18-8C4E-6086D9DC0DE3} 3: 1 
1: The action 'Install' for product 'MySQL Server 8.0.34' completed successfully.
