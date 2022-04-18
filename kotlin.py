breakConstant = "x"
language = "kt"

domainName = input("input domain name:")
paramsDomainName = domainName.lower()
prefix = input("input prefix(optional):")

# Create Domain Layer
print("create domain model file")
f = open(f"./{prefix}{domainName}.{language}", "w")
print("input fieldName and Type ex) name:String")
print("input x:x then stopped")

domainClassName = prefix + domainName
f.write(f"data class {domainClassName} (\n")
while True:
	fieldName, typeOfField = map(str, input().split(":"))
	if fieldName == breakConstant or typeOfField == breakConstant:
	    break
	f.write(f"val {fieldName}:{typeOfField},\n")
f.write(")\n")
f.close()

print("create domain repository file")
repositoryClassName = prefix+domainName+"Repository"
f = open(f"./{repositoryClassName}.{language}", "w")
f.write(f"interface {repositoryClassName} {{\n")
f.write(f"fun fetch{domainName}s(): Single<List<{domainName}>>\n")
f.write(f"fun save{domainName}s({paramsDomainName}s: List<{domainName}>): Completable\n")
f.write(f"fun delete{domainName}s({paramsDomainName}s: List<{domainName}>): Completable\n")
f.write("}\n")
f.close()

print("create domain usecase file")
saveUseCaseClassName = prefix+"Save"+domainName+"UseCase"
f = open(f"./{saveUseCaseClassName}.{language}", "w")
f.write(f"class {saveUseCaseClassName}(\nprivate val repository: {repositoryClassName}\n) {{\n")
f.write(f"fun invoke({paramsDomainName}s: List<{domainName}>): Completable {{ }}\n")
f.write("}\n")
f.close()

fetchUseCaseClassName = prefix+"Fetch"+domainName+"UseCase"
f = open(f"./{fetchUseCaseClassName}.{language}", "w")
f.write(f"class {fetchUseCaseClassName}(\nprivate val repository: {repositoryClassName}\n) {{\n")
f.write(f"fun invoke(): Single<List<{domainName}>> {{ }}\n")
f.write("}\n")
f.close()

deleteUseCaseClassName = prefix+"Delete"+domainName+"UseCase"
f = open(f"./{deleteUseCaseClassName}.{language}", "w")
f.write(f"class {deleteUseCaseClassName}(\nprivate val repository: {repositoryClassName}\n) {{\n")
f.write(f"fun invoke({paramsDomainName}s: List<{domainName}>): Completable {{ }}\n")
f.write("}\n")
f.close()


# Create Data Layer
print("create data source file")
dataSourceClassName = prefix+domainName+"DataSource"
f = open(f"./{dataSourceClassName}.{language}", "w")
f.write(f"interface {dataSourceClassName} {{\n")
f.write(f"fun fetch{domainName}s(): Single<List<{domainName}>>\n")
f.write(f"fun save{domainName}s({paramsDomainName}s: List<{domainName}>): Completable\n")
f.write(f"fun delete{domainName}s({paramsDomainName}s: List<{domainName}>): Completable\n")
f.write("}\n")
f.close()

remoteDataSourceClassName = prefix+domainName+"RemoteDataSource"
f = open(f"./{remoteDataSourceClassName}.{language}", "w")
f.write(f"class {remoteDataSourceClassName}(): {dataSourceClassName} {{\n")
f.write(f"override fun fetch{domainName}s(): Single<List<{domainName}>> {{}}\n")
f.write(f"override fun save{domainName}s({paramsDomainName}s: List<{domainName}>): Completable {{}}\n")
f.write(f"override fun delete{domainName}s({paramsDomainName}s: List<{domainName}>): Completable {{}}\n")
f.write("}\n")
f.close()

localDataSourceClassName = prefix+domainName+"LocalDataSource"
f = open(f"./{localDataSourceClassName}.{language}", "w")
f.write(f"class {localDataSourceClassName}(): {dataSourceClassName} {{\n")
f.write(f"override fun fetch{domainName}s(): Single<List<{domainName}>> {{}}\n")
f.write(f"override fun save{domainName}s({paramsDomainName}s: List<{domainName}>): Completable {{}}\n")
f.write(f"override fun delete{domainName}s({paramsDomainName}s: List<{domainName}>): Completable {{}}\n")
f.write("}\n")
f.close()

print("create data repository file")
dataRepositoryClassName = prefix+domainName+"RepositoryImpl"
f = open(f"./{dataRepositoryClassName}.{language}", "w")
f.write(f"class {dataRepositoryClassName}(\nprivate val remoteDataSource: {remoteDataSourceClassName},\nprivate val localDataSource: {localDataSourceClassName}\n): {repositoryClassName} {{\n")
f.write(f"override fun fetch{domainName}s(): Single<List<{domainName}>> {{}}\n")
f.write(f"override fun save{domainName}s({paramsDomainName}s: List<{domainName}>): Completable {{}}\n")
f.write(f"override fun delete{domainName}s({paramsDomainName}s: List<{domainName}>): Completable {{}}\n")
f.write("}\n")
f.close()
