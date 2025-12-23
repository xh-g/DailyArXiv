#!/usr/bin/env python3
"""
Test script to verify DailyArXiv setup
"""

import sys
import os
import importlib.util

# Constants
MAX_DISPLAY_LENGTH = 80

def test_imports():
    """Test that all required modules can be imported"""
    print("Testing imports...")
    required_modules = ['easydict', 'feedparser', 'pytz']
    
    for module in required_modules:
        spec = importlib.util.find_spec(module)
        if spec is None:
            print(f"  ❌ {module} - NOT INSTALLED")
            return False
        else:
            print(f"  ✅ {module} - installed")
    return True

def test_project_files():
    """Test that all required files exist"""
    print("\nTesting project files...")
    required_files = [
        'main.py',
        'utils.py', 
        'requirements.txt',
        'README.md',
        'SETUP.md',
        '.github/workflows/update.yaml',
        '.github/ISSUE_TEMPLATE.md'
    ]
    
    all_exist = True
    for file in required_files:
        if os.path.exists(file):
            print(f"  ✅ {file} - exists")
        else:
            print(f"  ❌ {file} - MISSING")
            all_exist = False
    return all_exist

def test_utils():
    """Test utility functions"""
    print("\nTesting utility functions...")
    try:
        from utils import get_daily_date, generate_table
        from easydict import EasyDict
        
        # Test date function
        date_str = get_daily_date()
        print(f"  ✅ get_daily_date() works: {date_str}")
        
        # Test table generation
        mock_paper = EasyDict({
            'Title': 'Test Paper',
            'Link': 'https://arxiv.org/abs/1234.5678',
            'Date': '2025-12-23T00:00:00Z',
            'Comment': 'Test'
        })
        table = generate_table([mock_paper])
        print(f"  ✅ generate_table() works: {len(table)} chars generated")
        
        return True
    except Exception as e:
        print(f"  ❌ Error: {e}")
        return False

def test_configuration():
    """Test main.py configuration"""
    print("\nTesting main.py configuration...")
    try:
        with open('main.py', 'r') as f:
            content = f.read()
            
        # Check if keywords are defined
        if 'keywords = [' in content:
            # Extract keywords line
            for line in content.split('\n'):
                if line.strip().startswith('keywords = ['):
                    display_text = line.strip()
                    if len(display_text) > MAX_DISPLAY_LENGTH:
                        display_text = display_text[:MAX_DISPLAY_LENGTH] + "..."
                    else:
                        display_text = display_text + "..."
                    print(f"  ✅ Keywords configured: {display_text}")
                    break
        
        # Check max_result
        if 'max_result = ' in content:
            for line in content.split('\n'):
                if line.strip().startswith('max_result = '):
                    print(f"  ✅ {line.strip()}")
                    break
                    
        return True
    except Exception as e:
        print(f"  ❌ Error: {e}")
        return False

def main():
    print("=" * 60)
    print("DailyArXiv Setup Verification")
    print("=" * 60)
    
    tests = [
        test_imports,
        test_project_files,
        test_utils,
        test_configuration
    ]
    
    results = [test() for test in tests]
    
    print("\n" + "=" * 60)
    if all(results):
        print("✅ All tests passed! Your setup is ready to use.")
        print("\nNext steps:")
        print("1. Customize keywords in main.py")
        print("2. Run: python main.py")
        print("3. Check README.md for results")
    else:
        print("❌ Some tests failed. Please check the errors above.")
        sys.exit(1)
    print("=" * 60)

if __name__ == '__main__':
    main()
