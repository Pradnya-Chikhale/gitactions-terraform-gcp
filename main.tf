resource "google_storage_bucket" "my-bucket" {
  name                     = "githubdemo-bucket"
  project                  = "vital-petal-409810"
  location                 = "US"
  force_destroy            = true
  public_access_prevention = "enforced"
}