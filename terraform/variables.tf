variable "credentials" {
  description = "My Credentials"
  default     = "/Users/ama/.google/credentials/google_credentials_ngu_a.json"
  #ex: if you have a directory where this file is called keys with your service account json file
  #saved there as my-creds.json you could use default = "./keys/my-creds.json"
}


variable "project" {
  description = "data-pipes-a"
  default     = "data-pipes-a"
}

variable "region" {
  description = "Region"
  #Update the below to your desired region
  default     = "europe-west2"
}

variable "location" {
  description = "Project Location"
  #Update the below to your desired location
  default     = "EU"
}

variable "bq_dataset_name" {
  description = "My BigQuery Dataset Name"
  #Update the below to what you want your dataset to be called
  default     = "data_set_weather"
}

variable "gcs_bucket_name" {
  description = "My Storage Bucket Name"
  #Update the below to a unique bucket name
  default     = "weather_bucket_2024_01_08"
}

variable "gcs_storage_class" {
  description = "Bucket Storage Class"
  default     = "STANDARD"
}