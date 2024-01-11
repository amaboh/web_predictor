terraform {
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "5.6.0"
    }
  }
}

provider "google" {
  credentials = file(var.credentials)
  project     = var.project
  region      = var.region
}


resource "google_storage_bucket" "data_lake-bucket" {
  name          = "${var.gcs_bucket_name}_${var.project}"
  location      = var.location
  force_destroy = true

  #Optional, but recommended settings;
  storage_class = var.gcs_storage_class
  uniform_bucket_level_access = true

    versioning {
    enabled     = true
  }


  lifecycle_rule {
    condition {
      age = 1
    }
    action {
      type = "AbortIncompleteMultipartUpload"
    }
    
  }

    
}



resource "google_bigquery_dataset" "demo_dataset" {
  dataset_id = var.bq_dataset_name
  location   = var.location
}