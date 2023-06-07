require 'azure/storage/blob'

ACCOUNT_NAME = ENV['ACCOUNT_NAME']
ACCOUNT_KEY = ENV['ACCOUNT_KEY']

puts ACCOUNT_NAME
puts ACCOUNT_KEY

blob_client = Azure::Storage::Blob::BlobService.create(
  storage_account_name: ACCOUNT_NAME,
  storage_access_key: ACCOUNT_KEY
)

puts blob_client

blob_client.list_containers().each do |container|
    puts container.name
    blob_client.list_blobs(container.name).each do |blob|
      puts "-> #{blob.name}"
    end
end

blob_client.create_container("some-conatainer-name")
