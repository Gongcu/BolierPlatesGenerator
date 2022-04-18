def isReferenceType(typeOfField: str):
	return "*" in typeOfField

breakConstant = "x"
header = "h"
impl = "m"
language = "kt"

domainName = input("input domain name:")
paramsDomainName = domainName.lower()
prefix = input("input prefix(optional):")

# Create Domain Layer
print("input fieldName and Type ex) name:String")
print("input x:x then stopped")

# ------ Domain Model --------

#header
properties = list()
f = open(f"./{prefix}{domainName}.{header}", "w")
domainClassName = prefix + domainName
f.write(f"@import Foundation;\n\n")
f.write(f"NS_ASSUME_NONNULL_BEGIN\n\n")
f.write(f"@interface {domainClassName} : NSObject\n\n")
while True:
    fieldName, typeOfField = map(str, input().split(":"))
    if fieldName == breakConstant or typeOfField == breakConstant:
        break
    properties.append((fieldName,typeOfField))
    if isReferenceType(typeOfField):
        f.write(f"@property (nonatomic, copy, readonly) {typeOfField} {fieldName};\n")
    else:
        f.write(f"@property (assign, readonly) {typeOfField} {fieldName};\n")
f.write("\n")

for index, item in enumerate(properties):
	fieldName, typeOfField = item
	if index == 0:
	   	f.write(f"- (instancetype)initWith{fieldName.title()}:({typeOfField}){fieldName}\n")
	else:
	    f.write(f"{fieldName}:({typeOfField}){fieldName}\n")
f.write(";\n")
f.write("@end\n\n")
f.write("NS_ASSUME_NONNULL_END\n")
f.close()

#impl
f = open(f"./{prefix}{domainName}.{impl}", "w")
f.write(f"#import <{domainClassName}.{header}>\n\n")
f.write(f"@implementation {domainClassName}\n\n")
for index, (fieldName, typeOfField) in enumerate(properties):
	if index == 0:
		f.write(f"- (instancetype)initWith{fieldName.title()}:({typeOfField}){fieldName}\n")
	else:
		f.write(f"{fieldName}:({typeOfField}){fieldName}\n")
f.write(f"{{")
f.write(f"if (self = [self init]) {{")
for index, (fieldName, typeOfField) in enumerate(properties):
	f.write(f"_{fieldName} = {fieldName};\n")
f.write(f"}}\n")
f.write(f"return self;\n")
f.write(f"}}")
f.write("\n\n")
f.write("@end\n\n")
f.close()

# ------ Domain Repository --------

#header
repositoryClassName = prefix+domainName+"Repository"
f = open(f"./{repositoryClassName}.{header}", "w")
f.write(f"@import Foundation;\n")
f.write(f"@import ReactiveObjC;\n\n")
f.write(f"@class {domainClassName};\n\n")
f.write(f"NS_ASSUME_NONNULL_BEGIN\n\n")
f.write(f"@protocol {repositoryClassName} <NSObject>\n\n")
f.write(f"- (RACSignal<NSArray<{domainClassName} *> *> *)fetch{domainName}s;")
f.write(f"- (RACSignal *)save{domainName}s(NSArray<{domainName} *> *){paramsDomainName}s;")
f.write(f"- (RACSignal *)delete{domainName}s(NSArray<{domainName} *> *){paramsDomainName}s;")
f.write("@end\n\n")
f.write("NS_ASSUME_NONNULL_END\n")
f.close()

# --------- Use Case ----------
#[SaveUseCase]
#header
saveUseCaseClassName = prefix+"Save"+domainName+"UseCase"
f = open(f"./{saveUseCaseClassName}.{header}", "w")
f.write(f"@import Foundation;\n")
f.write(f"@import ReactiveObjC;\n\n")
f.write(f"@class {domainClassName};\n")
f.write(f"@protocol {repositoryClassName};\n\n")
f.write(f"NS_ASSUME_NONNULL_BEGIN\n\n")
f.write(f"@interface {saveUseCaseClassName} : NSObject\n\n")
f.write(f"- (instancetype)initWithRepository:(id<{repositoryClassName}>)repository;\n\n")
f.write(f"- (RACSignal *)executeWith{paramsDomainName.title()}s:(NSArray<{domainName} *> *){paramsDomainName}s\n\n")
f.write("@end\n\n")
f.write("NS_ASSUME_NONNULL_END\n")
f.close()

#impl
f = open(f"./{saveUseCaseClassName}.{impl}", "w")
f.write(f"#import <{saveUseCaseClassName}.{header}>\n")
f.write(f"#import <{domainClassName}.{header}>\n")
f.write(f"#import <{repositoryClassName}.{header}>\n\n")

f.write(f"@implementation {saveUseCaseClassName} {{\n")
f.write(f"id<{repositoryClassName}> _repository;\n")
f.write(f"}}\n\n")
f.write(f"- (instancetype)initWithRepository:(id<{repositoryClassName}>)repository {{\n")
f.write(f"if (self = [super init]) {{\n_repository = repository;\n}}\n")
f.write(f"return self;\n")
f.write(f"}}\n\n")
f.write(f"- (RACSignal *)executeWith{paramsDomainName.title()}s:(NSArray<{domainName} *> *){paramsDomainName}s {{ }}\n\n")
f.write("@end\n\n")
f.write("NS_ASSUME_NONNULL_END\n")
f.close()


#[FetchUseCase]
#header
fetchUseCaseClassName = prefix+"Fetch"+domainName+"UseCase"
f = open(f"./{fetchUseCaseClassName}.{header}", "w")
f.write(f"@import Foundation;\n")
f.write(f"@import ReactiveObjC;\n\n")
f.write(f"@class {domainClassName};\n")
f.write(f"@protocol {repositoryClassName};\n\n")
f.write(f"NS_ASSUME_NONNULL_BEGIN\n\n")
f.write(f"@interface {fetchUseCaseClassName} : NSObject\n\n")
f.write(f"- (instancetype)initWithRepository:(id<{repositoryClassName}>)repository;\n\n")
f.write(f"- (RACSignal<NSArray<{domainClassName} *> *> *)execute;\n\n")
f.write("@end\n\n")
f.write("NS_ASSUME_NONNULL_END\n")
f.close()

#impl
f = open(f"./{fetchUseCaseClassName}.{impl}", "w")
f.write(f"#import <{fetchUseCaseClassName}.{header}>\n")
f.write(f"#import <{domainClassName}.{header}>\n")
f.write(f"#import <{repositoryClassName}.{header}>\n\n")

f.write(f"@implementation {fetchUseCaseClassName} {{\n")
f.write(f"id<{repositoryClassName}> _repository;\n")
f.write(f"}}\n\n")
f.write(f"- (instancetype)initWithRepository:(id<{repositoryClassName}>)repository {{\n")
f.write(f"if (self = [super init]) {{\n_repository = repository;\n}}\n")
f.write(f"return self;\n")
f.write(f"}}\n\n")
f.write(f"- (RACSignal<NSArray<{domainClassName} *> *> *)execute {{ }}\n\n")
f.write("@end\n\n")
f.write("NS_ASSUME_NONNULL_END\n")
f.close()

#[DeleteUseCase]
#header
deleteUseCaseClassName = prefix+"Delete"+domainName+"UseCase"
f = open(f"./{deleteUseCaseClassName}.{header}", "w")
f.write(f"@import Foundation;\n")
f.write(f"@import ReactiveObjC;\n\n")
f.write(f"@class {domainClassName};\n")
f.write(f"@protocol {repositoryClassName};\n\n")
f.write(f"NS_ASSUME_NONNULL_BEGIN\n\n")
f.write(f"@interface {deleteUseCaseClassName} : NSObject\n\n")
f.write(f"- (instancetype)initWithRepository:(id<{repositoryClassName}>)repository;\n\n")
f.write(f"- (RACSignal *)executeWith{paramsDomainName.title()}s:(NSArray<{domainName} *> *){paramsDomainName}s\n\n")
f.write("@end\n\n")
f.write("NS_ASSUME_NONNULL_END\n")
f.close()

#impl
f = open(f"./{deleteUseCaseClassName}.{impl}", "w")
f.write(f"#import <{deleteUseCaseClassName}.{header}>\n")
f.write(f"#import <{domainClassName}.{header}>\n")
f.write(f"#import <{repositoryClassName}.{header}>\n\n")

f.write(f"@implementation {deleteUseCaseClassName} {{\n")
f.write(f"id<{repositoryClassName}> _repository;\n")
f.write(f"}}\n\n")
f.write(f"- (instancetype)initWithRepository:(id<{repositoryClassName}>)repository {{\n")
f.write(f"if (self = [super init]) {{\n_repository = repository;\n}}\n")
f.write(f"return self;\n")
f.write(f"}}\n\n")
f.write(f"- (RACSignal *)executeWith{paramsDomainName.title()}s:(NSArray<{domainName} *> *){paramsDomainName}s {{ }}\n\n")
f.write("@end\n\n")
f.write("NS_ASSUME_NONNULL_END\n")
f.close()




# -------- Data Layer --------
#[DataSource]
#header
dataSourceClassName = prefix+domainName+"DataSource"
f = open(f"./{dataSourceClassName}.{header}", "w")
f.write(f"@import Foundation;\n")
f.write(f"@import ReactiveObjC;\n\n")
f.write(f"@class {domainClassName};\n\n")
f.write(f"NS_ASSUME_NONNULL_BEGIN\n\n")
f.write(f"@protocol {dataSourceClassName} <NSObject>\n\n")
f.write(f"- (RACSignal<NSArray<{domainClassName} *> *> *)fetch{domainName}s;\n")
f.write(f"- (RACSignal *)save{domainName}s(NSArray<{domainName} *> *){paramsDomainName}s;\n")
f.write(f"- (RACSignal *)delete{domainName}s(NSArray<{domainName} *> *){paramsDomainName}s;\n")
f.write("@end\n\n")
f.write("NS_ASSUME_NONNULL_END\n")
f.close()


#[RemoteDataSource]
#header
remoteDataSourceClassName = prefix+domainName+"RemoteDataSource"
f = open(f"./{remoteDataSourceClassName}.{header}", "w")
f.write(f"@import Foundation;\n")
f.write(f"@import ReactiveObjC;\n\n")
f.write(f"@class {domainClassName};\n")
f.write(f"@protocol ServiceApi;\n\n")
f.write(f"NS_ASSUME_NONNULL_BEGIN\n\n")
f.write(f"@interface {remoteDataSourceClassName} : NSObject<{dataSourceClassName}>\n\n")
f.write(f"- (instancetype)initWithServiceApi:(id<ServiceApi>)serviceApi;\n\n")
f.write("@end\n\n")
f.write("NS_ASSUME_NONNULL_END\n")
f.close()

#impl
f = open(f"./{remoteDataSourceClassName}.{impl}", "w")
f.write(f"#import <{remoteDataSourceClassName}.{header}>\n")
f.write(f"#import <{domainClassName}.{header}>\n")
f.write(f"#import <ServiceApi.{header}>\n\n")

f.write(f"@implementation {remoteDataSourceClassName} {{\n")
f.write(f"id<ServiceApi> _serviceApi;\n")
f.write(f"}}\n\n")
f.write(f"- (instancetype)initWithServiceApi:(id<ServiceApi>)serviceApi {{\n")
f.write(f"if (self = [super init]) {{\n_serviceApi = serviceApi;\n}}\n")
f.write(f"return self;\n")
f.write(f"}}\n\n")
f.write(f"- (RACSignal<NSArray<{domainClassName} *> *> *)fetch{domainName}s {{}}\n")
f.write(f"- (RACSignal *)save{domainName}s(NSArray<{domainName} *> *){paramsDomainName}s {{}}\n")
f.write(f"- (RACSignal *)delete{domainName}s(NSArray<{domainName} *> *){paramsDomainName}s {{}}\n\n")
f.write("@end\n\n")
f.write("NS_ASSUME_NONNULL_END\n")
f.close()

#[LocalDataSource]
#header
localDataSourceClassName = prefix+domainName+"LocalDataSource"
f = open(f"./{localDataSourceClassName}.{header}", "w")
f.write(f"@import Foundation;\n")
f.write(f"@import ReactiveObjC;\n\n")
f.write(f"@class {domainClassName};\n")
f.write(f"@protocol Database;\n\n")
f.write(f"NS_ASSUME_NONNULL_BEGIN\n\n")
f.write(f"@interface {localDataSourceClassName} : NSObject<{dataSourceClassName}>\n\n")
f.write(f"- (instancetype)initWithDatabase:(id<Database>)database;\n\n")
f.write("@end\n\n")
f.write("NS_ASSUME_NONNULL_END\n")
f.close()

#impl
f = open(f"./{localDataSourceClassName}.{impl}", "w")
f.write(f"#import <{localDataSourceClassName}.{header}>\n")
f.write(f"#import <{domainClassName}.{header}>\n")
f.write(f"#import <Database.{header}>\n\n")
f.write(f"@implementation {localDataSourceClassName} {{\n")
f.write(f"id<Database> _database;\n")
f.write(f"}}\n\n")
f.write(f"- (instancetype)initWithServiceApi:(id<Database>)database {{\n")
f.write(f"if (self = [super init]) {{\n _database = database; }}\n")
f.write(f"return self;\n")
f.write(f"}}\n\n")
f.write(f"- (RACSignal<NSArray<{domainClassName} *> *> *)fetch{domainName}s {{}}\n")
f.write(f"- (RACSignal *)save{domainName}s(NSArray<{domainName} *> *){paramsDomainName}s {{}}\n")
f.write(f"- (RACSignal *)delete{domainName}s(NSArray<{domainName} *> *){paramsDomainName}s {{}}\n\n")
f.write("@end\n\n")
f.write("NS_ASSUME_NONNULL_END\n")
f.close()


#[Repository]
#header
dataRepositoryClassName = prefix+domainName+"RepositoryImpl"
f = open(f"./{dataRepositoryClassName}.{header}", "w")
f.write(f"@import Foundation;\n")
f.write(f"@import ReactiveObjC;\n\n")
f.write(f"@class {domainClassName};\n")
f.write(f"@protocol Database;\n\n")
f.write(f"NS_ASSUME_NONNULL_BEGIN\n\n")
f.write(f"@interface {dataRepositoryClassName} : NSObject<{dataSourceClassName}>\n\n")
f.write(f"- (instancetype)initWithDatabase:(id<Database>)database;\n\n")
f.write("@end\n\n")
f.write("NS_ASSUME_NONNULL_END\n")
f.close()

#impl
f = open(f"./{dataRepositoryClassName}.{impl}", "w")
f.write(f"#import <{dataRepositoryClassName}.{header}>\n")
f.write(f"#import <{dataSourceClassName}.{header}>\n")
f.write(f"#import <{domainClassName}.{header}>\n")
f.write(f"@implementation {dataRepositoryClassName} {{\n")
f.write(f"id<{dataSourceClassName}> _remoteDataSource;\n")
f.write(f"id<{dataSourceClassName}> _localDataSource;\n")
f.write(f"}}\n\n")
f.write(f"- (instancetype)initWithRemoteDataSource:(id<{dataSourceClassName}>)remoteDataSource\n")
f.write(f"localDataSource:(id<{dataSourceClassName}>localDataSource) {{\n")
f.write(f"if (self = [super init]) {{\n")
f.write(f"_remoteDataSource = remoteDataSource;\n_localDataSource = localDataSource;\n}}\n")
f.write(f"return self;\n")
f.write(f"}}\n\n")
f.write(f"- (RACSignal<NSArray<{domainClassName} *> *> *)fetch{domainName}s {{}}\n")
f.write(f"- (RACSignal *)save{domainName}s(NSArray<{domainName} *> *){paramsDomainName}s {{}}\n")
f.write(f"- (RACSignal *)delete{domainName}s(NSArray<{domainName} *> *){paramsDomainName}s {{}}\n")
f.write("@end\n\n")
f.write("NS_ASSUME_NONNULL_END\n")
f.close()
