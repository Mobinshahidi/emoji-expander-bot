import os
import re
import logging
from telegram import Update, InlineQueryResultArticle, InputTextMessageContent
from telegram.ext import Application, InlineQueryHandler, ContextTypes
import emoji
import uuid

# Configure logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Persian emoji mapping
PERSIAN_EMOJI_MAP = {
    'لبخند': '😄',
    'خنده': '😂',
    'آتش': '🔥',
    'تایید': '👍',
    'گریه': '😢',
    'قلب': '❤️',
    'عشق': '💕',
    'ستاره': '⭐',
    'خورشید': '☀️',
    'ماه': '🌙',
    'گل': '🌹',
    'درخت': '🌳',
    'سگ': '🐶',
    'گربه': '🐱',
    'خانه': '🏠',
    'ماشین': '🚗',
    'هواپیما': '✈️',
    'قایق': '⛵',
    'کتاب': '📚',
    'موبایل': '📱',
    'کامپیوتر': '💻',
    'ایمیل': '📧',
    'تلفن': '📞',
    'ساعت': '⏰',
    'تقویم': '📅',
    'پول': '💰',
    'هدیه': '🎁',
    'جشن': '🎉',
    'موسیقی': '🎵',
    'فوتبال': '⚽',
    'پیتزا': '🍕',
    'چای': '🍵',
    'قهوه': '☕',
    'کیک': '🎂',
    'سیب': '🍎',
    'موز': '🍌',
    'انگور': '🍇',
    'هندوانه': '🍉',
    'نان': '🍞',
    'برنج': '🍚',
    'ماهی': '🐟',
    'مرغ': '🐔',
    'گوشت': '🥩',
    'سبزی': '🥬',
    'هویج': '🥕',
    'سیب‌زمینی': '🥔',
    'پیاز': '🧅',
    'سیر': '🧄',
    'فلفل': '🌶️',
    'خیار': '🥒',
    'گوجه': '🍅',
    'بادمجان': '🍆',
    'ذرت': '🌽',
    'قارچ': '🍄',
    'آناناس': '🍍',
    'نارگیل': '🥥',
    'آووکادو': '🥑',
    'توت‌فرنگی': '🍓',
    'گیلاس': '🍒',
    'هلو': '🍑',
    'خوشحال': '😊',
    'ناراحت': '😞',
    'عصبانی': '😠',
    'تعجب': '😮',
    'خسته': '😴',
    'بیمار': '🤒',
    'عینک': '🤓',
    'کلاه': '👒',
    'لباس': '👕',
    'کفش': '👞',
    'ساک': '👜',
    'انگشتر': '💍',
    'ساعت_مچی': '⌚',
    'عطر': '💄',
    'شامپو': '🧴',
    'صابون': '🧼',
    'حوله': '🏖️',
    'تخت': '🛏️',
    'صندلی': '🪑',
    'میز': '🏓',
    'تلویزیون': '📺',
    'رادیو': '📻',
    'دوربین': '📷',
    'چتر': '☂️',
    'کیف': '💼',
    'قفل': '🔒',
    'کلید': '🔑',
    'چکش': '🔨',
    'پیچ‌گوشتی': '🔧',
    'قیچی': '✂️',
    'چاقو': '🔪',
    'شمع': '🕯️',
    'لامپ': '💡',
    'باتری': '🔋',
    'پلاگ': '🔌',
    'آینه': '🪞',
    'پنجره': '🪟',
    'در': '🚪',
    'تصویر': '🖼️',
    'نقشه': '🗺️',
    'پرچم': '🏁',
    'بالن': '🎈',
    'عروسک': '🪆',
    'بازی': '🎮',
    'تاس': '🎲',
    'پازل': '🧩',
    'توپ': '⚾',
    'تنیس': '🎾',
    'بسکتبال': '🏀',
    'والیبال': '🏐',
    'راگبی': '🏈',
    'گلف': '⛳',
    'تیر': '🏹',
    'ماهیگیری': '🎣',
    'شنا': '🏊',
    'دوچرخه': '🚴',
    'اسکی': '⛷️',
    'کوهنوردی': '🧗'
}

def expand_emoji_shorthand(text: str) -> str:
    """
    Expand emoji shorthands in text to actual emojis.
    Supports both English (:smile:) and Persian (:لبخند:) formats.
    Also supports multipliers like :smile3 or :لبخند2 (number at the end)
    """
    logger.info(f"Input text: '{text}'")
    
    def replace_shorthand(match):
        full_match = match.group(0)
        emoji_name = match.group(1)
        multiplier = match.group(2) if len(match.groups()) > 1 and match.group(2) else None
        
        logger.info(f"Match found - Full: '{full_match}', Name: '{emoji_name}', Multiplier: '{multiplier}'")
        
        # Remove any trailing colons from emoji_name
        emoji_name = emoji_name.strip(':')
        
        # Parse multiplier
        count = 1
        if multiplier:
            try:
                count = int(multiplier)
                count = max(1, min(count, 10))  # Limit between 1-10
                logger.info(f"Multiplier parsed: {count}")
            except ValueError:
                count = 1
        
        # Try to get emoji
        emoji_char = None
        
        # First try Persian mapping
        if emoji_name in PERSIAN_EMOJI_MAP:
            emoji_char = PERSIAN_EMOJI_MAP[emoji_name]
            logger.info(f"Found Persian emoji: '{emoji_name}' -> '{emoji_char}'")
        else:
            # Try English emoji conversion
            try:
                emoji_char = emoji.emojize(f':{emoji_name}:', language='en')
                # If it didn't convert (still has colons), it's not a valid emoji
                if emoji_char.startswith(':') and emoji_char.endswith(':'):
                    emoji_char = None
                    logger.info(f"English emoji not found: '{emoji_name}'")
                else:
                    logger.info(f"Found English emoji: '{emoji_name}' -> '{emoji_char}'")
            except:
                emoji_char = None
                logger.info(f"Error converting English emoji: '{emoji_name}'")
        
        # Return the result
        if emoji_char:
            result = emoji_char * count
            logger.info(f"Final result: '{result}' (repeated {count} times)")
            return result
        else:
            logger.info(f"No emoji found, returning original: '{full_match}'")
            return full_match
    
    # Single pattern that handles both cases:
    # :smile3: or :smile3 (with number) OR :smile: or :smile (without number)
    pattern = r':([a-zA-Z\u0600-\u06FF_]+)(\d+)?:?'
    
    logger.info(f"Using pattern: {pattern}")
    result = re.sub(pattern, replace_shorthand, text)
    
    logger.info(f"Final output: '{result}'")
    return result

async def inline_query(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle the inline query."""
    if not update.inline_query:
        return
        
    query = update.inline_query.query
    
    if not query:
        return
    
    # Expand emoji shorthands
    expanded_text = expand_emoji_shorthand(query)
    
    # Create inline result
    results = [
        InlineQueryResultArticle(
            id=str(uuid.uuid4()),
            title="Expanded Emojis",
            description=f"Click to send: {expanded_text}",
            input_message_content=InputTextMessageContent(
                message_text=expanded_text
            )
        )
    ]
    
    await update.inline_query.answer(results)

def main() -> None:
    """Start the bot."""
    # Get bot token from environment variable
    token = os.getenv('BOT_TOKEN')
    if not token:
        logger.error("BOT_TOKEN environment variable not set!")
        return
    
    # Create the Application with proxy support (uncomment if needed)
    # proxy_url = "http://your-proxy:port"  # or socks5://your-proxy:port
    application = Application.builder().token(token).build()
    
    # If you need proxy, use this instead:
    # from telegram.request import HTTPXRequest
    # request = HTTPXRequest(proxy=proxy_url)
    # application = Application.builder().token(token).request(request).build()
    
    # Add handlers
    application.add_handler(InlineQueryHandler(inline_query))
    
    # Get port from environment variable or use default
    port = int(os.getenv('PORT', 8000))
    
    # Start the bot
    # Use polling for simplicity (works without webhook setup)
    logger.info("Starting bot with polling...")
    application.run_polling()

if __name__ == '__main__':
    main()
