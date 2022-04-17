breakConstant = "x"
language = "swift"

domainName = input("input domain name:")
paramsDomainName = domainName.lower()
prefix = input("input prefix(optional):")

# Create Domain Layer
print("create domain model file")
f = open(f"./{prefix}{domainName}.{language}", "w")
print("input fieldName and Type ex) name:String")
print("input x:x then stopped")

domainClassName = prefix + domainName
f.write(f"struct {domainClassName} (\n")
while True:
    fieldName, typeOfField = map(str, input().split(":"))
    if fieldName == breakConstant or typeOfField == breakConstant:
        break
    f.write(f"let {fieldName}:{typeOfField},\n")
f.write(")\n")
f.close()

print("create domain repository file")
repositoryClassName = prefix+domainName+"Repository"
f = open(f"./{repositoryClassName}.{language}", "w")
f.write(f"protocol {repositoryClassName} {{\n")
f.write(f"func fetch{domainName}s() -> Single<[{domainName}]>\n")
f.write(f"func save{domainName}s({paramsDomainName}s: [{domainName}]) -> Completable {{}}\n")
f.write(f"func delete{domainName}s({paramsDomainName}s: [{domainName}]) -> Completable {{}}\n")
f.write("}\n")
f.close()

print("create domain usecase file")
saveUseCaseClassName = prefix+"Save"+domainName+"UseCase"
f = open(f"./{saveUseCaseClassName}.{language}", "w")
f.write(f"final class {saveUseCaseClassName} {{\n")
f.write(f"private let repository: {repositoryClassName} {{\n")
f.write(f"init(repository: {repositoryClassName}) {{ self.repository = repository }}\n")
f.write(f"func invoke({paramsDomainName}s: [{domainName}]) -> Completable {{ }}\n")
f.write("}\n")
f.close()

fetchUseCaseClassName = prefix+"Fetch"+domainName+"UseCase"
f = open(f"./{fetchUseCaseClassName}.{language}", "w")
f.write(f"final class {fetchUseCaseClassName} {{\n")
f.write(f"private let repository: {repositoryClassName} {{\n")
f.write(f"init(repository: {repositoryClassName}) {{ self.repository = repository }}\n")
f.write(f"func invoke() -> Single<[{domainName}]> {{ }}\n")
f.write("}\n")
f.close()

deleteUseCaseClassName = prefix+"Delete"+domainName+"UseCase"
f = open(f"./{deleteUseCaseClassName}.{language}", "w")
f.write(f"final class {deleteUseCaseClassName} {{\n")
f.write(f"private let repository: {repositoryClassName} {{\n")
f.write(f"init(repository: {repositoryClassName}) {{ self.repository = repository }}\n")
f.write(f"func invoke({paramsDomainName}s: [{domainName}]) -> Completable {{ }}\n")
f.write("}\n")
f.close()


# Create Data Layer
print("create data source file")
dataSourceClassName = prefix+domainName+"DataSoure"
f = open(f"./{dataSourceClassName}.{language}", "w")
f.write(f"protocol {dataSourceClassName} {{\n")
f.write(f"func fetch{domainName}s() -> Single<[{domainName}]>\n")
f.write(f"func save{domainName}s({paramsDomainName}s: [{domainName}]) -> Completable {{}}\n")
f.write(f"func delete{domainName}s({paramsDomainName}s: [{domainName}]) -> Completable {{}}\n")
f.write("}\n")
f.close()

remoteDataSourceClassName = prefix+domainName+"RemoteDataSoure"
f = open(f"./{remoteDataSourceClassName}.{language}", "w")
f.write(f"final class {remoteDataSourceClassName}(): {dataSourceClassName} {{\n")
f.write(f"override func fetch{domainName}s() -> Single<[{domainName}]> {{}}\n")
f.write(f"override func save{domainName}s({paramsDomainName}s: [{domainName}]) -> Completable {{}}\n")
f.write(f"override func delete{domainName}s({paramsDomainName}s: [{domainName}]) -> Completable {{}}\n")
f.write("}\n")
f.close()

localDataSourceClassName = prefix+domainName+"LocalDataSoure"
f = open(f"./{localDataSourceClassName}.{language}", "w")
f.write(f"final class {localDataSourceClassName}(): {dataSourceClassName} {{\n")
f.write(f"override func fetch{domainName}s() -> Single<[{domainName}]> {{}}\n")
f.write(f"override func save{domainName}s({paramsDomainName}s: [{domainName}]) -> Completable {{}}\n")
f.write(f"override func delete{domainName}s({paramsDomainName}s: [{domainName}]) -> Completable {{}}\n")
f.write("}\n")
f.close()

print("create data repository file")
dataRepositoryClassName = prefix+domainName+"RepositoryImpl"
f = open(f"./{dataRepositoryClassName}.{language}", "w")
f.write(f"final class {dataRepositoryClassName}: {repositoryClassName} {{\n")
f.write(f"private let remoteDataSource: {remoteDataSourceClassName}\n")
f.write(f"private let localDataSource: {localDataSourceClassName}\n")
f.write(f"init(remoteDataSource: {remoteDataSourceClassName}, localDataSource: {localDataSourceClassName}) {{\n")
f.write(f"self.remotDataSource = remoteDataSource\n")
f.write(f"self.localDataSource = localDataSource\n")
f.write(f"}}\n")
f.write(f"override func fetch{domainName}s() -> Single<[{domainName}]> {{}}\n")
f.write(f"override func save{domainName}s({paramsDomainName}s: [{domainName}]) -> Completable {{}}\n")
f.write(f"override func delete{domainName}s({paramsDomainName}s:[{domainName}]) -> Completable {{}}\n")
f.write("}\n")
f.close()