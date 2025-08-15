#!/usr/bin/env python3
"""
Test Docker setup for Yoruba Language API.
"""

import subprocess
import time
import requests
import sys


def run_command(command, check=True):
    """Run a shell command and return the result."""
    try:
        result = subprocess.run(
            command, shell=True, check=check, capture_output=True, text=True
        )
        return result.returncode == 0, result.stdout, result.stderr
    except subprocess.CalledProcessError as e:
        return False, e.stdout, e.stderr


def check_docker():
    """Check if Docker is available."""
    print("🐳 Checking Docker availability...")
    success, stdout, stderr = run_command("docker --version")
    if success:
        print(f"✅ Docker is available: {stdout.strip()}")
        return True
    else:
        print("❌ Docker is not available")
        print(f"Error: {stderr}")
        return False


def check_docker_compose():
    """Check if Docker Compose is available."""
    print("🐳 Checking Docker Compose availability...")
    success, stdout, stderr = run_command("docker-compose --version")
    if success:
        print(f"✅ Docker Compose is available: {stdout.strip()}")
        return True
    else:
        print("❌ Docker Compose is not available")
        print(f"Error: {stderr}")
        return False


def build_docker_image():
    """Build the Docker image."""
    print("🔨 Building Docker image...")
    success, stdout, stderr = run_command(
        "docker build -t yoruba-language-api:test ."
    )
    if success:
        print("✅ Docker image built successfully")
        return True
    else:
        print("❌ Failed to build Docker image")
        print(f"Error: {stderr}")
        return False


def run_docker_container():
    """Run the Docker container."""
    print("🚀 Starting Docker container...")
    
    # Stop any existing container
    run_command("docker stop yoruba-test || true", check=False)
    run_command("docker rm yoruba-test || true", check=False)
    
    # Run new container
    success, stdout, stderr = run_command(
        "docker run -d --name yoruba-test -p 8001:8000 "
        "yoruba-language-api:test"
    )
    
    if success:
        print("✅ Docker container started successfully")
        return True
    else:
        print("❌ Failed to start Docker container")
        print(f"Error: {stderr}")
        return False


def wait_for_api():
    """Wait for the API to be ready."""
    print("⏳ Waiting for API to be ready...")
    
    max_attempts = 30
    attempt = 0
    
    while attempt < max_attempts:
        try:
            response = requests.get("http://localhost:8001/health", timeout=5)
            if response.status_code == 200:
                print("✅ API is ready!")
                return True
        except requests.exceptions.RequestException:
            pass
        
        attempt += 1
        time.sleep(2)
        print(f"  Attempt {attempt}/{max_attempts}...")
    
    print("❌ API failed to start within expected time")
    return False


def test_api_endpoints():
    """Test basic API endpoints."""
    print("🧪 Testing API endpoints...")
    
    base_url = "http://localhost:8001"
    
    # Test health endpoint
    try:
        response = requests.get(f"{base_url}/health")
        if response.status_code == 200:
            print("✅ Health endpoint working")
        else:
            print(f"❌ Health endpoint failed: {response.status_code}")
            return False
    except Exception as e:
        print(f"❌ Health endpoint error: {e}")
        return False
    
    # Test root endpoint
    try:
        response = requests.get(f"{base_url}/")
        if response.status_code == 200:
            print("✅ Root endpoint working")
        else:
            print(f"❌ Root endpoint failed: {response.status_code}")
            return False
    except Exception as e:
        print(f"❌ Root endpoint error: {e}")
        return False
    
    # Test translations endpoint
    try:
        response = requests.get(f"{base_url}/api/v1/translations")
        if response.status_code == 200:
            print("✅ Translations endpoint working")
        else:
            print(f"❌ Translations endpoint failed: {response.status_code}")
            return False
    except Exception as e:
        print(f"❌ Translations endpoint error: {e}")
        return False
    
    return True


def cleanup():
    """Clean up test resources."""
    print("🧹 Cleaning up test resources...")
    run_command("docker stop yoruba-test || true", check=False)
    run_command("docker rm yoruba-test || true", check=False)
    run_command("docker rmi yoruba-language-api:test || true", check=False)
    print("✅ Cleanup completed")


def main():
    """Main test function."""
    print("🧪 Yoruba Language API - Docker Test Suite")
    print("=" * 50)
    
    try:
        # Check prerequisites
        if not check_docker():
            sys.exit(1)
        
        if not check_docker_compose():
            sys.exit(1)
        
        # Build and test
        if not build_docker_image():
            sys.exit(1)
        
        if not run_docker_container():
            sys.exit(1)
        
        if not wait_for_api():
            cleanup()
            sys.exit(1)
        
        if not test_api_endpoints():
            cleanup()
            sys.exit(1)
        
        print("\n🎉 All Docker tests passed!")
        print("✅ Container is running and API is responding")
        print("🌐 API is available at: http://localhost:8001")
        print("📚 API docs at: http://localhost:8001/docs")
        
        # Keep container running for manual testing
        print("\n📝 Container will keep running for manual testing.")
        print("Run 'docker stop yoruba-test' to stop it.")
        print("Run 'docker logs yoruba-test' to view logs.")
        
    except KeyboardInterrupt:
        print("\n\n⚠️  Test interrupted by user")
        cleanup()
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")
        cleanup()
        sys.exit(1)


if __name__ == "__main__":
    main()
