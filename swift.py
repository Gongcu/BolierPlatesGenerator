import os
import command

breakConstant = "x"
language = "swift"

domainGroupFolderName = "Domain"
modelFolderName = "Model"
repositoryFolderName = "Repository"
usecaseFolderName = "UseCase"
infrastructureGroupFolderName = "Infrastructure"
dataSourceFolderName = "DataSource"

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
f.write(f"import Foundation\n\n")
f.write(f"struct {domainClassName} {{\n")
while True:
	fieldName, typeOfField = map(str, input().split(":"))
	if fieldName == breakConstant or typeOfField == breakConstant:
	    break
	f.write(f"  let {fieldName}: {typeOfField}\n")
f.write("}\n")
f.close()

print("create domain repository file")
repositoryClassName = prefix+domainName+"Repository"
f = open(f"./{domainGroupFolderName}/{repositoryFolderName}/{repositoryClassName}.{language}", "w")
f.write(f"import BuzzRxSwift\n\n")
f.write(f"protocol {repositoryClassName} {{\n")
if command.read():
	f.write(f"  func fetch{domainName}s() -> Observable<[{domainName}]>\n")
if command.create():
	f.write(f"  func save{domainName}s({paramsDomainName}s: [{domainName}]) -> Observable<Void>\n")
if command.delete():
	f.write(f"  func delete{domainName}s({paramsDomainName}s: [{domainName}]) -> Observable<Void>\n")
f.write("}\n")
f.close()

print("create domain usecase file")
if command.read():
	fetchUseCaseClassName = prefix+"Fetch"+domainName+"UseCase"
	f = open(f"./{domainGroupFolderName}/{usecaseFolderName}/{fetchUseCaseClassName}.{language}", "w")
	f.write(f"import BuzzRxSwift\n\n")
	f.write(f"class {fetchUseCaseClassName} {{\n")
	f.write(f"  private let repository: {repositoryClassName}\n\n")
	f.write(f"  init(repository: {repositoryClassName}) {{ self.repository = repository }}\n\n")
	f.write(f"  func execute() -> Observable<[{domainName}]> {{ }}\n")
	f.write("}\n")
	f.close()

if command.create():
	saveUseCaseClassName = prefix+"Save"+domainName+"UseCase"
	f = open(f"./{domainGroupFolderName}/{usecaseFolderName}/{saveUseCaseClassName}.{language}", "w")
	f.write(f"import BuzzRxSwift\n\n")
	f.write(f"class {saveUseCaseClassName} {{\n")
	f.write(f"  private let repository: {repositoryClassName}\n\n")
	f.write(f"  init(repository: {repositoryClassName}) {{ self.repository = repository }}\n\n")
	f.write(f"  func execute({paramsDomainName}s: [{domainName}]) -> Observable<Void> {{ }}\n")
	f.write("}\n")
	f.close()

if command.delete():
	deleteUseCaseClassName = prefix+"Delete"+domainName+"UseCase"
	f = open(f"./{domainGroupFolderName}/{usecaseFolderName}/{deleteUseCaseClassName}.{language}", "w")
	f.write(f"import BuzzRxSwift\n\n")
	f.write(f"class {deleteUseCaseClassName} {{\n")
	f.write(f"  private let repository: {repositoryClassName}\n\n")
	f.write(f"  init(repository: {repositoryClassName}) {{ self.repository = repository }}\n\n")
	f.write(f"  func execute({paramsDomainName}s: [{domainName}]) -> Observable<Void> {{ }}\n")
	f.write("}\n")
	f.close()

# Create Data Layer
os.makedirs(f"./{infrastructureGroupFolderName}", exist_ok=True)
os.makedirs(f"./{infrastructureGroupFolderName}/{repositoryFolderName}", exist_ok=True)
os.makedirs(f"./{infrastructureGroupFolderName}/{dataSourceFolderName}", exist_ok=True)

print("create data source file")
dataSourceClassName = prefix+domainName+"DataSource"
f = open(f"./{infrastructureGroupFolderName}/{dataSourceFolderName}/{dataSourceClassName}.{language}", "w")
f.write(f"import BuzzRxSwift\n\n")
f.write(f"protocol {dataSourceClassName} {{\n")
if command.read():
	f.write(f"  func fetch{domainName}s() -> Observable<[{domainName}]>\n")
if command.create():
	f.write(f"  func save{domainName}s({paramsDomainName}s: [{domainName}]) -> Observable<Void>\n")
if command.delete():
	f.write(f"  func delete{domainName}s({paramsDomainName}s: [{domainName}]) -> Observable<Void>\n")
f.write("}\n")
f.close()

remoteDataSourceClassName = prefix+domainName+"RemoteDataSource"
f = open(f"./{infrastructureGroupFolderName}/{dataSourceFolderName}/{remoteDataSourceClassName}.{language}", "w")
f.write(f"import BuzzRxSwift\n\n")
f.write(f"class {remoteDataSourceClassName}(): {dataSourceClassName} {{\n")
if command.read():
	f.write(f"  override func fetch{domainName}s() -> Observable<[{domainName}]> {{}}\n")
if command.create():
	f.write(f"  override func save{domainName}s({paramsDomainName}s: [{domainName}]) -> Observable<Void> {{}}\n")
if command.delete():
	f.write(f"  override func delete{domainName}s({paramsDomainName}s: [{domainName}]) -> Observable<Void> {{}}\n")
f.write("}\n")
f.close()

localDataSourceClassName = prefix+domainName+"LocalDataSource"
f = open(f"./{infrastructureGroupFolderName}/{dataSourceFolderName}/{localDataSourceClassName}.{language}", "w")
f.write(f"import BuzzRxSwift\n\n")
f.write(f"class {localDataSourceClassName}(): {dataSourceClassName} {{\n")
if command.read():
	f.write(f"  override func fetch{domainName}s() -> Observable<[{domainName}]> {{}}\n")
if command.create():
	f.write(f"  override func save{domainName}s({paramsDomainName}s: [{domainName}]) -> Observable<Void> {{}}\n")
if command.delete():
	f.write(f"  override func delete{domainName}s({paramsDomainName}s: [{domainName}]) -> Observable<Void> {{}}\n")
f.write("}\n")
f.close()

print("create data repository file")
dataRepositoryClassName = prefix+domainName+"RepositoryImpl"
f = open(f"./{infrastructureGroupFolderName}/{repositoryFolderName}/{dataRepositoryClassName}.{language}", "w")
f.write(f"import BuzzRxSwift\n\n")
f.write(f"class {dataRepositoryClassName}: {repositoryClassName} {{\n")
f.write(f"  private let remoteDataSource: {remoteDataSourceClassName}\n")
f.write(f"  private let localDataSource: {localDataSourceClassName}\n\m")
f.write(f"  init(remoteDataSource: {remoteDataSourceClassName}, localDataSource: {localDataSourceClassName}) {{\n")
f.write(f"    self.remotDataSource = remoteDataSource\n")
f.write(f"    self.localDataSource = localDataSource\n")
f.write(f"  }}\n\n")
if command.read():
	f.write(f"  override func fetch{domainName}s() -> Observable<[{domainName}]> {{}}\n")
if command.create():
	f.write(f"  override func save{domainName}s({paramsDomainName}s: [{domainName}]) -> Observable<Void> {{}}\n")
if command.delete():
	f.write(f"  override func delete{domainName}s({paramsDomainName}s:[{domainName}]) -> Observable<Void> {{}}\n")
f.write("}\n")
f.close()
