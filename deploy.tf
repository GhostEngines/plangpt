// INIT

terraform {
  required_providers {
    digitalocean = {
      source = "digitalocean/digitalocean"
      version = "~> 2.0"
    }
    # github = {
    #   source  = "integrations/github"
    #   version = "~> 5.0"
    # }
  }
}

// SET VARIABLES

variable "do_api_token" {
  type        = string
  description = "DigitalOcean API key."
}

variable "OPENAI_API_KEY" {
  type        = string
  description = "OpenAI API key"
}

# variable "gh_access_token" {
#   type        = string
#   description = "GitHub Personal Access Token"
# }


// CONFIGURE PROVIDERS

# provider "github" {
#     token = var.gh_access_token
# }

provider "digitalocean" {
  token = var.do_api_token
}


// RESOURCES

resource "digitalocean_app" "plan_gpt" {
  spec {
    name = "plan-gpt"
    region = "nyc"

    service {
        name = "web"
        dockerfile_path = "./Dockerfile" 
        github {
            branch = "main"
            deploy_on_push = true
            repo = "GhostEngines/plangpt"
        }
        env {
            key = "OPENAI_API_KEY"
            value = var.OPENAI_API_KEY
        }
    }    
  }
}