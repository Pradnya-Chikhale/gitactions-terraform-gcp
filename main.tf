#resource "google_storage_bucket" "my-bucket" {
#  name                     = "githubdemo-bucket"
# project                  = "vital-petal-409810"
#  location                 = "US"
#  force_destroy            = true
#  public_access_prevention = "enforced"
#}

provider "google" {
  credentials = file("terraform.json")
  project     = "vital-petal-409810"
  region      = "us-central1"
}
resource "google_cloud_run_service" "django_app" {
  name     = "django-app"
  location = "us-central1"
  template {
    spec {
      containers {
        image = "gcr.io/vital-petal-409810/gitactions-terraform-app"
      }
    }
  }
}