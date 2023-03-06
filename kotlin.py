import os
import sys
import command

breakConstant = "x"
language = "kt"

domainGroupFolderName = "domain"
modelFolderName = "model"
repositoryFolderName = "repository"
usecaseFolderName = "usecase"
infrastructureGroupFolderName = "infrastructure"
dataSourceFolderName = "datasource"

domainName = input("input domain name:")
paramsDomainName = domainName.lower()
prefix = input("input prefix(optional):")

# Create Domain Layer
print("create domain model file")
os.makedirs(f"./{domainGroupFolderName}", exist_ok=True)
os.makedirs(f"./{domainGroupFolderName}/{modelFolderName}", exist_ok=True)
os.makedirs(f"./{domainGroupFolderName}/{repositoryFolderName}", exist_ok=True)
os.makedirs(f"./{domainGroupFolderName}/{usecaseFolderName}", exist_ok=True)

f = open(f"./{domainGroupFolderName}/{modelFolderName}/{prefix}{domainName}.{language}", "w")
print("input fieldName and Type ex) name:String")
print("input x:x then stopped")

domainClassName = prefix + domainName
f.write(f"data class {domainClassName} (\n")
while True:
	fieldName, typeOfField = map(str, input().split(":"))
	if fieldName == breakConstant or typeOfField == breakConstant:
	    break
	f.write(f"\tval {fieldName}: {typeOfField},\n")
f.write(")\n")
f.close()

print("create domain repository file")
repositoryClassName = prefix+domainName+"Repository"
f = open(f"./{domainGroupFolderName}/{repositoryFolderName}/{repositoryClassName}.{language}", "w")
f.write(f"interface {repositoryClassName} {{\n")
if command.read():
	f.write(f"\tfun fetch{domainName}s(): Single<List<{domainName}>>\n")
if command.create():
	f.write(f"\tfun save{domainName}s({paramsDomainName}s: List<{domainName}>): Completable\n")
if command.delete():
	f.write(f"\tfun delete{domainName}s({paramsDomainName}s: List<{domainName}>): Completable\n")
f.write("}\n")
f.close()

print("create domain usecase file")
if command.read():
	fetchUseCaseClassName = prefix+"Fetch"+domainName+"UseCase"
	f = open(f"./{domainGroupFolderName}/{usecaseFolderName}/{fetchUseCaseClassName}.{language}", "w")
	f.write(f"class {fetchUseCaseClassName}(\n\tprivate val repository: {repositoryClassName}\n) {{\n")
	f.write(f"\toperator fun invoke(): Single<List<{domainName}>> {{ }}\n")
	f.write("}\n")
	f.close()

if command.create():
	saveUseCaseClassName = prefix+"Save"+domainName+"UseCase"
	f = open(f"./{domainGroupFolderName}/{usecaseFolderName}/{saveUseCaseClassName}.{language}", "w")
	f.write(f"class {saveUseCaseClassName}(\n\tprivate val repository: {repositoryClassName}\n) {{\n")
	f.write(f"\toperator fun invoke({paramsDomainName}s: List<{domainName}>): Completable {{ }}\n")
	f.write("}\n")
	f.close()

if command.delete():
	deleteUseCaseClassName = prefix+"Delete"+domainName+"UseCase"
	f = open(f"./{domainGroupFolderName}/{usecaseFolderName}/{deleteUseCaseClassName}.{language}", "w")
	f.write(f"class {deleteUseCaseClassName}(\n\tprivate val repository: {repositoryClassName}\n) {{\n")
	f.write(f"\toperator fun invoke({paramsDomainName}s: List<{domainName}>): Completable {{ }}\n")
	f.write("}\n")
	f.close()


# Create Data Layer
os.makedirs(f"./{infrastructureGroupFolderName}", exist_ok=True)
os.makedirs(f"./{infrastructureGroupFolderName}/{repositoryFolderName}", exist_ok=True)
os.makedirs(f"./{infrastructureGroupFolderName}/{dataSourceFolderName}", exist_ok=True)

print("create data source file")
dataSourceClassName = prefix+domainName+"DataSource"
f = open(f"./{infrastructureGroupFolderName}/{dataSourceFolderName}/{dataSourceClassName}.{language}", "w")
f.write(f"interface {dataSourceClassName} {{\n")
if command.read():
	f.write(f"\tfun fetch{domainName}s(): Single<List<{domainName}>>\n")
if command.create():
	f.write(f"\tfun save{domainName}s({paramsDomainName}s: List<{domainName}>): Completable\n")
if command.delete():
	f.write(f"\tfun delete{domainName}s({paramsDomainName}s: List<{domainName}>): Completable\n")
f.write("}\n")
f.close()

remoteDataSourceClassName = prefix+domainName+"RemoteDataSource"
f = open(f"./{infrastructureGroupFolderName}/{dataSourceFolderName}/{remoteDataSourceClassName}.{language}", "w")
f.write(f"class {remoteDataSourceClassName}(): {dataSourceClassName} {{\n")
if command.read():
	f.write(f"\toverride fun fetch{domainName}s(): Single<List<{domainName}>> {{}}\n")
if command.create():
	f.write(f"\toverride fun save{domainName}s({paramsDomainName}s: List<{domainName}>): Completable {{}}\n")
if command.delete():
	f.write(f"\toverride fun delete{domainName}s({paramsDomainName}s: List<{domainName}>): Completable {{}}\n")
f.write("}\n")
f.close()

localDataSourceClassName = prefix+domainName+"LocalDataSource"
f = open(f"./{infrastructureGroupFolderName}/{dataSourceFolderName}/{localDataSourceClassName}.{language}", "w")
f.write(f"class {localDataSourceClassName}(): {dataSourceClassName} {{\n")
if command.read():
	f.write(f"\toverride fun fetch{domainName}s(): Single<List<{domainName}>> {{}}\n")
if command.create():
	f.write(f"\toverride fun save{domainName}s({paramsDomainName}s: List<{domainName}>): Completable {{}}\n")
if command.delete():
	f.write(f"\toverride fun delete{domainName}s({paramsDomainName}s: List<{domainName}>): Completable {{}}\n")
f.write("}\n")
f.close()

print("create data repository file")
dataRepositoryClassName = prefix+domainName+"RepositoryImpl"
f = open(f"./{infrastructureGroupFolderName}/{repositoryFolderName}/{dataRepositoryClassName}.{language}", "w")
f.write(f"class {dataRepositoryClassName}(\n\tprivate val remoteDataSource: {remoteDataSourceClassName},\n\tprivate val localDataSource: {localDataSourceClassName}\n): {repositoryClassName} {{\n")
if command.read():
	f.write(f"\toverride fun fetch{domainName}s(): Single<List<{domainName}>> {{}}\n")
if command.create():
	f.write(f"\toverride fun save{domainName}s({paramsDomainName}s: List<{domainName}>): Completable {{}}\n")
if command.delete():
	f.write(f"\toverride fun delete{domainName}s({paramsDomainName}s: List<{domainName}>): Completable {{}}\n")
f.write("}\n")
f.close()
