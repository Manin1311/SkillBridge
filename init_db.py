"""
Database Initialization and Seeding Script

This script:
1. Creates database tables
2. Creates default admin user
3. Seeds initial categories and sample data

Author: SkillBridge Team
Purpose: Initialize database with default data
"""

import sys
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
if hasattr(sys.stderr, 'reconfigure'):
    sys.stderr.reconfigure(encoding='utf-8', errors='replace')

from models import db, User, Category, Service
from werkzeug.security import generate_password_hash


def create_default_admin(app):
    """
    Create default admin user if not exists
    
    Args:
        app: Flask application instance
    """
    with app.app_context():
        # Check if admin already exists
        admin = User.query.filter_by(email=app.config['ADMIN_EMAIL']).first()
        
        if not admin:
            # Create admin user
            admin = User(
                username='admin',
                email=app.config['ADMIN_EMAIL'],
                user_type='admin',
                full_name='System Administrator',
                is_active=True,
                is_verified=True
            )
            admin.set_password(app.config['ADMIN_PASSWORD'])
            
            db.session.add(admin)
            db.session.commit()
            
            print(f"✓ Admin user created: {app.config['ADMIN_EMAIL']}")
        else:
            print()
            # print(f"✓ Admin user already exists: {app.config['ADMIN_EMAIL']}")


def seed_categories():
    """
    Seed initial categories
    
    Creates default service categories with icons and colors
    """
    # Default categories matching the original design
    categories_data = [
        {
            'name': 'Web Development',
            'description': 'Website and web application development services',
            'icon': 'bi-code-slash',
            'color': 'bg-primary'
        },
        {
            'name': 'Graphic Design',
            'description': 'Logo, branding, and graphic design services',
            'icon': 'bi-palette',
            'color': 'bg-danger'
        },
        {
            'name': 'Content Writing',
            'description': 'SEO content, blog posts, and copywriting',
            'icon': 'bi-pen',
            'color': 'bg-warning'
        },
        {
            'name': 'Video Editing',
            'description': 'Professional video editing and production',
            'icon': 'bi-camera-video',
            'color': 'bg-info'
        },

        {
            'name': 'Music & Audio',
            'description': 'Music production, mixing, and audio services',
            'icon': 'bi-music-note-beamed',
            'color': 'bg-secondary'
        },
        {
            'name': 'Photography',
            'description': 'Professional photography services',
            'icon': 'bi-camera',
            'color': 'bg-dark'
        },
        {
            'name': 'Marketing',
            'description': 'Digital marketing and social media services',
            'icon': 'bi-graph-up-arrow',
            'color': 'bg-primary'
        }
    ]
    
    for cat_data in categories_data:
        # Check if category already exists
        existing = Category.query.filter_by(name=cat_data['name']).first()
        
        if not existing:
            category = Category(**cat_data)
            db.session.add(category)
    
    db.session.commit()
    print(f"✓ Seeded {len(categories_data)} categories")


def seed_sample_data():
    """
    Seed rich sample services, users, and categories for testing and demonstration
    """
    from models import Community, WebsiteReview

    # Create sample provider users across different domains
    sample_providers = [
        {
            'username': 'alex_dev',
            'email': 'alex@example.com',
            'password': 'password123',
            'user_type': 'provider',
            'full_name': 'Alex Chen',
            'bio': 'Full-stack web developer with 6+ years experience in React, Node, and Python'
        },
        {
            'username': 'sarah_design',
            'email': 'sarah@example.com',
            'password': 'password123',
            'user_type': 'provider',
            'full_name': 'Sarah Miller',
            'bio': 'Creative graphic designer & UI/UX specialist with 100+ brand launches'
        },
        {
            'username': 'james_writer',
            'email': 'james@example.com',
            'password': 'password123',
            'user_type': 'provider',
            'full_name': 'James Wilson',
            'bio': 'Senior SEO copywriter, blogger, and technical documentation author'
        },
        {
            'username': 'elena_video',
            'email': 'elena@example.com',
            'password': 'password123',
            'user_type': 'provider',
            'full_name': 'Elena Rostova',
            'bio': 'Video editor & motion graphics animator with expertise in Premiere & After Effects'
        },
        {
            'username': 'marcus_audio',
            'email': 'marcus@example.com',
            'password': 'password123',
            'user_type': 'provider',
            'full_name': 'Marcus Vance',
            'bio': 'Audio engineer & podcast producer offering pristine mixing and mastering'
        },
        {
            'username': 'david_photo',
            'email': 'david@example.com',
            'password': 'password123',
            'user_type': 'provider',
            'full_name': 'David Kim',
            'bio': 'Commercial photographer specializing in e-commerce product photos and portrait retouching'
        },
        {
            'username': 'priya_marketing',
            'email': 'priya@example.com',
            'password': 'password123',
            'user_type': 'provider',
            'full_name': 'Priya Sharma',
            'bio': 'Digital growth marketer driving high ROI via meta ads, Google Ads, and technical SEO'
        }
    ]
    
    user_map = {}
    for user_data in sample_providers:
        user = User.query.filter_by(email=user_data['email']).first()
        if not user:
            user = User(
                username=user_data['username'],
                email=user_data['email'],
                user_type=user_data['user_type'],
                full_name=user_data['full_name'],
                bio=user_data['bio'],
                is_verified=True
            )
            user.set_password(user_data['password'])
            db.session.add(user)
            db.session.flush()
        user_map[user_data['username']] = user
    
    db.session.commit()

    # Retrieve categories
    cat_map = {c.name: c.id for c in Category.query.all()}
    
    # Define rich services across all categories
    services_to_seed = [
        # Web Development
        {
            'user_id': user_map['alex_dev'].id,
            'category_id': cat_map.get('Web Development', 1),
            'title': 'Custom Full-Stack Web App (React, Python & Node)',
            'description': 'I will build a high-performance, responsive web application tailored to your business needs with clean architecture, secure authentication, and seamless DB integration.',
            'price': 250.00,
            'delivery_time': '5 days',
            'tags': 'React, Python, Flask, Node.js, PostgreSQL, Tailwind'
        },
        {
            'user_id': user_map['alex_dev'].id,
            'category_id': cat_map.get('Web Development', 1),
            'title': 'E-Commerce Website & Shopify Store Setup',
            'description': 'Complete setup for your online store including payment gateway integration, product uploads, mobile responsiveness, and speed optimization.',
            'price': 180.00,
            'delivery_time': '4 days',
            'tags': 'Shopify, WooCommerce, E-Commerce, Stripe, Responsive'
        },

        # Graphic Design
        {
            'user_id': user_map['sarah_design'].id,
            'category_id': cat_map.get('Graphic Design', 2),
            'title': 'Modern Minimalist Logo & Brand Identity Package',
            'description': 'Get a professional, unique logo design complete with brand guidelines, color palettes, typography specs, and vector source files (AI, EPS, SVG, PNG).',
            'price': 95.00,
            'delivery_time': '3 days',
            'tags': 'Logo, Branding, Illustrator, Vector, Graphic Design'
        },
        {
            'user_id': user_map['sarah_design'].id,
            'category_id': cat_map.get('Graphic Design', 2),
            'title': 'Figma UI/UX Design for Mobile Apps & Websites',
            'description': 'Sleek, modern UI/UX design with interactive wireframes and components created in Figma. Ready for developer handoff.',
            'price': 140.00,
            'delivery_time': '4 days',
            'tags': 'UI/UX, Figma, Web Design, Mobile App, Prototype'
        },

        # Content Writing
        {
            'user_id': user_map['james_writer'].id,
            'category_id': cat_map.get('Content Writing', 3),
            'title': 'SEO Optimized Blog Posts, Articles & Copywriting',
            'description': 'Engaging, thoroughly researched, and SEO-optimized blog posts designed to rank high on Google search results and drive organic conversions.',
            'price': 45.00,
            'delivery_time': '2 days',
            'tags': 'SEO, Blog Post, Content Writing, Copywriting, Marketing'
        },
        {
            'user_id': user_map['james_writer'].id,
            'category_id': cat_map.get('Content Writing', 3),
            'title': 'Technical Writing, API Docs & Whitepapers',
            'description': 'Clear, precise technical documentation, software user manuals, whitepapers, and developer guides written for clarity.',
            'price': 120.00,
            'delivery_time': '3 days',
            'tags': 'Technical Writing, Documentation, API, Whitepaper'
        },

        # Video Editing
        {
            'user_id': user_map['elena_video'].id,
            'category_id': cat_map.get('Video Editing', 4),
            'title': 'Professional YouTube Video Editing & Color Grading',
            'description': 'Dynamic YouTube video editing with smooth transitions, motion graphics, sound effects, subtitles, and cinematic color grading.',
            'price': 85.00,
            'delivery_time': '3 days',
            'tags': 'Premiere Pro, After Effects, Video Editing, YouTube'
        },
        {
            'user_id': user_map['elena_video'].id,
            'category_id': cat_map.get('Video Editing', 4),
            'title': 'Viral Short-Form Reels, Shorts & TikTok Video Editing',
            'description': 'High-retention captions, sound design, hook animations, and pacing designed specifically for Instagram Reels, Shorts, and TikTok.',
            'price': 40.00,
            'delivery_time': '1 day',
            'tags': 'Reels, TikTok, Shorts, Captions, Viral Video'
        },

        # Music & Audio
        {
            'user_id': user_map['marcus_audio'].id,
            'category_id': cat_map.get('Music & Audio', 5),
            'title': 'Podcast Audio Cleaning, Editing & Vocal Mixing',
            'description': 'Remove background noise, umms, pauses, and echo. Professional equalization, compression, and loudness normalization for broadcast quality.',
            'price': 60.00,
            'delivery_time': '2 days',
            'tags': 'Podcast, Audio Editing, Vocal Mixing, Audio Cleanup'
        },

        # Photography
        {
            'user_id': user_map['david_photo'].id,
            'category_id': cat_map.get('Photography', 6),
            'title': 'Product Photo Editing, Background Removal & Retouching',
            'description': 'Flawless product photo retouching for Amazon, Shopify, and social media. Includes background removal, shadow creation, and color correction.',
            'price': 35.00,
            'delivery_time': '1 day',
            'tags': 'Photoshop, Product Photography, Background Removal, Retouching'
        },

        # Marketing
        {
            'user_id': user_map['priya_marketing'].id,
            'category_id': cat_map.get('Marketing', 7),
            'title': 'Social Media Ads Campaign & Growth Strategy',
            'description': 'End-to-end Meta (Facebook/Instagram) and Google Ads campaign setup, audience targeting, ad copy, and performance analytics setup.',
            'price': 110.00,
            'delivery_time': '3 days',
            'tags': 'Digital Marketing, Meta Ads, Google Ads, Growth, Strategy'
        }
    ]

    for s_data in services_to_seed:
        existing_service = Service.query.filter_by(title=s_data['title']).first()
        if not existing_service:
            service = Service(**s_data)
            db.session.add(service)

    # Seed Communities
    sample_communities = [
        {
            'name': 'Full-Stack Web Developers',
            'description': 'A vibrant group for web developers sharing React, Node, Python, and modern web frameworks knowledge.',
            'category': 'Web Development',
            'image_url': 'default-community.png'
        },
        {
            'name': 'UI/UX & Brand Designers Guild',
            'description': 'Connect with creative designers, share Figma prototypes, discuss typography, and receive feedback on your designs.',
            'category': 'Graphic Design',
            'image_url': 'default-community.png'
        },
        {
            'name': 'Content Creators & Copywriters',
            'description': 'Exchange SEO techniques, content strategy tips, and copywriting masterclasses with industry peers.',
            'category': 'Content Writing',
            'image_url': 'default-community.png'
        },
        {
            'name': 'Video Editors & Motion Artists',
            'description': 'Discuss Premiere Pro tricks, After Effects templates, color grading presets, and video production workflows.',
            'category': 'Video Editing',
            'image_url': 'default-community.png'
        },
        {
            'name': 'Growth Hackers & Digital Marketers',
            'description': 'Share ad strategies, SEO audit checklists, social media trends, and conversion rate optimization tips.',
            'category': 'Marketing',
            'image_url': 'default-community.png'
        }
    ]

    for c_data in sample_communities:
        existing_comm = Community.query.filter_by(name=c_data['name']).first()
        if not existing_comm:
            comm = Community(**c_data)
            db.session.add(comm)

    # Seed Website Feedback / Reviews
    sample_reviews = [
        {
            'name': 'Rohit Verma',
            'email': 'rohit@example.com',
            'suggestion': 'SkillBridge made it incredibly easy to hire a freelance React developer for our startup. Smooth contract signing and chat experience!',
            'rating': 5
        },
        {
            'name': 'Ananya Patel',
            'email': 'ananya@example.com',
            'suggestion': 'The platform interface is modern, fast, and intuitive. Great community section to connect with fellow designers.',
            'rating': 5
        },
        {
            'name': 'Vikram Singh',
            'email': 'vikram@example.com',
            'suggestion': 'Loved the digital contract signing with timestamp verification. Provides great safety for freelancers.',
            'rating': 5
        }
    ]

    for r_data in sample_reviews:
        existing_rev = WebsiteReview.query.filter_by(name=r_data['name']).first()
        if not existing_rev:
            rev = WebsiteReview(**r_data)
            db.session.add(rev)

    db.session.commit()
    print("✓ Successfully seeded rich services, communities, and reviews into database!")


if __name__ == '__main__':
    """
    Run this script directly to initialize database
    """
    from app import create_app
    
    app = create_app()
    
    with app.app_context():
        # Create all tables
        db.create_all()
        print("✓ Database tables created")
        
        # Create admin
        create_default_admin(app)
        
        # Seed categories
        seed_categories()
        
        # Seed sample data
        seed_sample_data()
        
        print("\n✓ Database initialization complete!")
        print(f"Admin login: {app.config['ADMIN_EMAIL']} / {app.config['ADMIN_PASSWORD']}")
